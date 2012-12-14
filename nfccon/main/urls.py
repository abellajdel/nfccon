from django.conf.urls import patterns, url, include
from rest_framework.urlpatterns import format_suffix_patterns
from main.views import OneItem


urlpatterns = patterns('main.views',
    url(r'^oneitem/(?P<id>\d+)/$', OneItem.as_view(), name='one item'),
)

# Format suffixes
urlpatterns = format_suffix_patterns(urlpatterns)
