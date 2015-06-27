from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'puzzle.views.home', name='home'),
    url(r'^helloworld/$', 'puzzle.views.helloworld', name='helloword'),	
)
