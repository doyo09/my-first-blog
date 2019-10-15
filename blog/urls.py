from django.conf.urls import url
from django.contrib import admin
from blog.views import post_list1, post_detail, post_new, post_edit, item_request, board, issue, board_detail,\
    issue_detail, item_request_detail, board_edit, board_new, item_request_new, item_request_edit, issue_new, issue_edit

urlpatterns = [


    # "blog" APP의 url등록

    url(r'^$', post_list1, name="blog"),
    url(r'^post/(?P<pk>[0-9]+)/$', post_detail, name='post_detail'),
    url(r'^post/new/$', post_new, name='post_new'),
    url(r'^post/(?P<pk>[0-9]+)/edit', post_edit, name='post_edit'),

    # item_request
    url(r'^ItemRequest/$', item_request, name='item_request'),
    url(r'^ItemRequest/(?P<pk>[0-9]+)/$', item_request_detail, name='item_request_detail'),
    url(r'^ItemRequest/new/$', item_request_new, name='item_request_new'),
    url(r'^ItemRequest/(?P<pk>[0-9]+)/edit', item_request_edit, name='item_request_edit'),

    # board
    url(r'^board/$', board, name='board'),
    url(r'^board/(?P<pk>[0-9]+)/$', board_detail, name='board_detail'),
    url(r'^board/new/$', board_new, name='board_new'),
    url(r'^board/(?P<pk>[0-9]+)/edit', board_edit, name='board_edit'),


    # issue
    url(r'^issues/$', issue, name='issue'),
    url(r'^issues/(?P<pk>[0-9]+)/$', issue_detail, name='issue_detail'),
    url(r'^issues/new/$', issue_new, name='issue_new'),
    url(r'^issues/(?P<pk>[0-9]+)/edit', issue_edit, name='issue_edit'),

]