from django.conf.urls.defaults import patterns, include, url
from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib import admin
from rapidsms_httprouter.urls import urlpatterns as router_urls
from relay.views import submissions,approve,proxy,send_messages
from rapidsms_httprouter.views import  console
from rapidsms.lib.urls.login_logout import urlpatterns as wtf

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
     url(r'^submissions/?$', submissions, name='rapidsms-dashboard'),
    url(r'^messages/?$', send_messages, name='contacts'),
    url(r'^proxy/.', proxy, name='proxy'),
    url(r"^submissions/(?P<payment_pk>\d+)/approve/$", approve, name="approve"),
    url("^router/console", console, {}, 'httprouter-console'),

)+router_urls+wtf

from rapidsms_httprouter.router import get_router
#router=get_router()