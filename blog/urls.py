#coding: utf-8
from django.conf.urls import url, include

from blog.views import PostsListView, PostDetailView, signup, activate

urlpatterns = [
url(r'^$', PostsListView.as_view(), name='list'),
url(r'^(?P<pk>\d+)/$', PostDetailView.as_view()),
url(r'^signup/$', signup, name='signup'),
url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
	activate, name='activate'),
url(r'^comments/', include('django_comments.urls')),
]
