from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin

import auth_ex.views

from haystack.forms import FacetedSearchForm
from haystack.query import SearchQuerySet
from haystack.views import FacetedSearchView

sqs = SearchQuerySet().facet('type').facet('location')


urlpatterns = [
    url(r'^admin/login/', auth_ex.views.login),
    url(r'^admin/', admin.site.urls),
    url(r'', include('blog.urls')),
    url(r'', include('articles.urls')),
    url(r'', include('comments.urls')),
    url(r'^search/', include('haystack.urls')),
]


if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += [
        url(r'^rosetta/', include('rosetta.urls')),
    ]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
