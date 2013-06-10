#!/usr/bin/python
# -*- coding: utf-8 -*-

from rapidsms_httprouter.models import Message
from rapidsms.models import Contact, Connection
from django.shortcuts import render_to_response,HttpResponse
from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger
from .models import MobilePayment,MLoan
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.test.client import Client
import urllib,urllib2
import requests
import json
import datetime


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



    return render_to_response("relay/submissions.html",{'payments':payments})

@csrf_exempt
def approve(request,payment_pk):
    from requests.auth import HTTPBasicAuth
    payment=MobilePayment.objects.get(pk=payment_pk)
    s = requests.Session()
    s.auth = (settings.USERNAME, settings.PASSWORD)

    s.headers.update({'x-test': 'true'})

    payment.approved=True
    client=payment.client
    loan_id=MLoan.objects.get(client=client).id
    post_url=settings.BASE_URL+"loans/%d/transactions?tenantIdentifier=default&command=repayment"%loan_id
    headers={"Content-type": "application/json"}
    now=datetime.datetime.now()

    post_dict={"locale": "en_GB","dateFormat": "dd MMMM yyyy","transactionDate": "%s"%now.strftime("%d %b %Y"),"transactionAmount": "%d"%payment.amount,"note": "Mobile Payment"}
    r=requests.post(post_url,json.dumps(dict(post_dict)),verify=False,headers=headers,auth=HTTPBasicAuth(settings.USERNAME, settings.PASSWORD),)
    return HttpResponse(r.content)

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
def contacts(request):
    return render_to_response("relay/contacts.html",{'contacts':None})



