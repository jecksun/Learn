from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'Site.views.home', name= 'home'),
    url(r'^about$', 'Site.views.about', name= 'about'),
    url(r'^article/(?P<article_id>[0-9]+)/$', 'Site.views.show_article', name= 'article'),
)