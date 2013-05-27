from django.conf.urls.defaults import patterns, include, url
from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib import admin
from rapidsms_httprouter.urls import urlpatterns as router_urls
from .relay.views import submissions,approve,proxy

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
     url(r'^submissions/?$', submissions, name='submissions'),
    url(r'^proxy/.', proxy, name='proxy'),
    url(r"^submissions/(?P<payment_pk>\d+)/approve/$", approve, name="approve"),

)+router_urls

from rapidsms_httprouter.router import get_router
#router=get_router()