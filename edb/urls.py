# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'edb.views.home', name='home'),
    # url(r'^edb/', include('edb.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include( admin.site.urls )),
    
    url(r'^populate/$', 'alpha.views.populate' ),
    url(r'^welcome/$', 'alpha.views.welcome' ),
    url(r'^loan/$', 'alpha.views.loan' ),
    url(r'^loan/process/$', 'alpha.views.process_loan' ),
    
)
