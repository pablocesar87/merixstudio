from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^articles/$', views.article_list, name='article_list'),
    url(r'^articles/article/(?P<pk>[0-9]+)/$', views.article_detail, name='article_detail'),
    url(r'^articles/article/new/$', views.article_new, name='article_new'),
    url(r'^articles/article/(?P<pk>[0-9]+)/edit/$', views.article_edit, name='article_edit'),
]