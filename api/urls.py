#coding: utf-8
from django.conf.urls import url
from .views import create_user, PostList

urlpatterns = [
url(r'^add_users/$', create_user, name='add_user'),
url(r'^posts$', PostList.as_view(), name='posts'),
]