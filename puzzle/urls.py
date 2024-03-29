from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'puzzle.views.home', name='home'),
    url(r'^helloworld/$', 'puzzle.views.helloworld', name='helloword'),
    url(r'^last/$', 'puzzle.views.last', name='last'),	
    url(r'^keepclicking/(?P<path>.*)$', 'puzzle.views.keepclicking', name='last'),	
    #url(r'^generate/$', 'puzzle.views.generate', name='generate'),
    #url(r'^deleteall/$', 'puzzle.views.deleteall', name='deleteall'),
    url(r'^check/$', 'puzzle.views.check', name='check'),
    url(r'^doge/$', 'puzzle.views.register', name='check'),
)
