from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^blog/$', views.post_list, name='post_list'),
    url(r'^blog/post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'^blog/post/new/$', views.post_new, name='post_new'),
    url(r'^blog/post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
]
