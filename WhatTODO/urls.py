from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView

from django.contrib.auth import views as auth_views
from django.contrib.auth import logout

from django.http import HttpResponseRedirect

from .api import TagList, TagDetail
from .api import TodoList, TodoDetail

from django.shortcuts import redirect

admin.autodiscover()

def logout_view (request):
    logout(request)
    return HttpResponseRedirect('/login')

class SimpleStaticView(TemplateView):
    def get_template_names(self):
        return [self.kwargs.get('template_name') + ".html"]
        
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            return redirect('/login')
            #return redirect('/login/?next=%s' % request.path)
        return super(SimpleStaticView, self).get(request, *args, **kwargs)

tag_urls = patterns('',
    url(r'^/(?P<pk>\d+)$', TagDetail.as_view(), name='tag-detail'),
    url(r'^$', TagList.as_view(), name='tag-list')
    )

todo_urls = patterns('',
    url(r'^/(?P<pk>\d+)$', TodoDetail.as_view(), name='todo-detail'),
    url(r'^$', TodoList.as_view(), name='todo-list')
    )

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'WhatTODO.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^api/tags', include(tag_urls)),
    url(r'^api/todos', include(todo_urls)),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^login', auth_views.login, {'template_name': 'login.html'}),
    url(r'^logout' , logout_view ),
    url(r'^$', SimpleStaticView.as_view(template_name='index.html'), name='WhatTODO'),
    url(r'^(?P<template_name>\w+)$', SimpleStaticView.as_view(), name='WhatTODO'),
)
