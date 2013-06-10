#!/usr/bin/python
# -*- coding: utf-8 -*-

from rapidsms_httprouter.models import Message
from rapidsms.models import Contact, Connection
from django.shortcuts import render_to_response,HttpResponse
from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger
from .models import MobilePayment,MLoan,MNote,MLoanRepaymentSchedule,MClient
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.test.client import Client
import requests
import json
import datetime
from rapidsms_httprouter.router import get_router
from rapidsms.models import Contact, Connection, Backend
from django import forms
from django.template import RequestContext



def clean_number(number):
    if number.startswith('0'):
        return '%s%s' % (256, number[1:])
    elif number.startswith('+'):
        return '%s' % number[1:]

def submissions(request):
    payment_list=MobilePayment.objects.order_by('-created')

    paginator = Paginator(payment_list, 25)
    page = request.GET.get('page',1)
    try:
        payments = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        payments = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        payments = paginator.page(paginator.num_pages)



    return render_to_response("relay/submissions.html",{'payments':payments},context_instance=RequestContext(request))

@csrf_exempt
def approve(request,payment_pk):
    from requests.auth import HTTPBasicAuth
    payment=MobilePayment.objects.get(pk=payment_pk)
    s = requests.Session()
    s.auth = (settings.USERNAME, settings.PASSWORD)
    s.headers.update({'x-test': 'true'})
    payment.approved=True
    payment.save()
    client=payment.client
    loan=MLoan.objects.get(client=client)
    no_ofpayements=loan.term_frequency
    principal=int(loan.principal_amount)
    loan_officer=loan.loan_officer_id
    payements_count=MNote.objects.filter(loan_id=loan.id,client_id=client.id).count()
    next_payement=MLoanRepaymentSchedule.objects.filter(installment=payements_count+1)[0]
    pm=int(MLoanRepaymentSchedule.objects.filter(loan_id=loan.id)[0].principal_amount)
    balance=(no_ofpayements-(payements_count+1))*pm
    message="Thanks %s for your payment of %d on %s. Your remaining balance is %d and your next payment is due %s"%(client.firstname,payment.amount,payment.created.strftime("%d %b %Y"),balance,next_payement.duedate.strftime("%d %b"))
    post_url=settings.BASE_URL+"loans/%d/transactions?tenantIdentifier=default&command=repayment"%loan.id
    headers={"Content-type": "application/json"}
    now=datetime.datetime.now()
    post_dict={"locale": "en_GB","dateFormat": "dd MMMM yyyy","transactionDate": "%s"%now.strftime("%d %b %Y"),"transactionAmount": "%d"%payment.amount,"note": "Mobile Payment"}
    r=requests.post(post_url,json.dumps(dict(post_dict)),verify=False,headers=headers,auth=HTTPBasicAuth(settings.USERNAME, settings.PASSWORD),)
    router = get_router()
    backend, created = Backend.objects.get_or_create(name="mifos")
    connection, created = Connection.objects.get_or_create(backend=backend, identity=payment.sender)
    msg1 = router.add_outgoing(connection, message)
    return HttpResponse(r.text)

@csrf_exempt
def proxy(request):
    import simplejson
    from requests.auth import HTTPBasicAuth
    base_url="https://151.236.219.158:8443/mifosng-provider/api/v1"
    parts=request.path.rsplit("/proxy")[1]
    args="?tenantIdentifier=default&"+request.META['QUERY_STRING']
    headers=request.META
    #headers={"Content-type": "x-mifos-platform-tenantid"}
    url=base_url+parts+args
    if request.GET.get('password'):
        r=requests.post(url,{},auth=HTTPBasicAuth(request.GET.get('username'), request.GET.get('password')),verify=False)
        d=r.content
        data = simplejson.loads(d)
        data['status']=1

        print d

        #print r.content
        print url
        xx=HttpResponse(simplejson.dumps(data),mimetype="application/json")

        xx["Access-Control-Allow-Methods"]="GET, POST, PUT, DELETE, OPTIONS,XMODIFY"
        #xx["Content-Disposition"]="application/json"
        xx["Access-Control-Allow-Origin"]="*"
        xx['Cache-Control'] = 'no-cache'
        xx['Access-Control-Max-Age']=123
        return xx
    if request.method == 'POST':
        r=requests.post(url,json.dumps(dict(request.POST)),headers,verify=False)
        return HttpResponse(r.content)
    else:
        r=requests.get(url,verify=False)
        print r.content
        return HttpResponse(r.content)


class MessageForm(forms.Form): # pragma: no cover
    text = forms.CharField(max_length=160, label="Message", widget=forms.TextInput(attrs={'size': '60'}))
    contacts = forms.ModelMultipleChoiceField(queryset=MClient.objects.all())

def send_messages(request):
    mform=MessageForm()
    if request.method == 'POST':
        mform = MessageForm(request.POST)
        if mform.is_valid():
            contacts=mform.cleaned_data['contacts']
            message=mform.cleaned_data['text']
            router = get_router()
            backend, created = Backend.objects.get_or_create(name="mifos")
            for m in contacts:
                try:
                    connection, created = Connection.objects.get_or_create(backend=backend, identity=clean_number(m.external_id))
                    router.add_outgoing(connection, message)
                except AttributeError:
                    pass
            return render_to_response("relay/contacts.html",{'mform':mform,'status':'Messages Sent'})

    return render_to_response("relay/contacts.html",{'mform':mform},context_instance=RequestContext(request))



