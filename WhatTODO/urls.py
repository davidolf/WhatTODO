from django.conf.urls import patterns, include, url

from .api import TagList, TagDetail
from .api import TodoList, TodoDetail

from django.contrib import admin
admin.autodiscover()

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

    url(r'^tags', include(tag_urls)),
    url(r'^todos', include(todo_urls)),

    url(r'^admin/', include(admin.site.urls)),
)
