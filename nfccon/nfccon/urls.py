from django.conf.urls import patterns, include, url
from django.views.generic.simple import direct_to_template

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'nfccon.views.home', name='home'),
    # url(r'^nfccon/', include('nfccon.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    (r'^accounts/', include('registration.urls')),
    (r'^$', direct_to_template, { 'template': 'index.html' }, 'index'),
    #nfccon Restful API urls
    url(r'^api/', include('main.urls')),
    url(r'^dashboard/', include('dashboard.urls')),
)
