# -*- coding:utf-8 -*- 
__author__ = 'll'
__date__ = '19-5-8 上午11:57'

from django.conf.urls import url
from .views import IndexView, CategoryView, PostView, SearchView, BlogListView, First, CommentView, WritePostView



urlpatterns = [

    url(r'^(?P<post_id>\d+)/$', PostView.as_view(), name='blogpost'),
    url(r'^category/(?P<category_id>\d+)/$', CategoryView.as_view(), name='category'),
    url(r'^search/$', SearchView.as_view(), name='search'),
    url(r'^postlist/$', BlogListView.as_view(), name='postlist'),
    url(r'^first/$', First.as_view()),
    url(r'^comment/(?P<post_id>\d+)/$', CommentView.as_view(), name='comment'),
    url(r'^writepost/', WritePostView.as_view(), name='writepost'),
]