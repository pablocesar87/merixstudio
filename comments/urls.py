from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^articles/article/(?P<pk>[0-9]+)/new_comment/$', views.article_new_comment, name='new_article_comment'),
    url(r'^blog/post/(?P<pk>[0-9]+)/new_comment/$', views.blog_new_comment, name='new_blog_comment'),
]
