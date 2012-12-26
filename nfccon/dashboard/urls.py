from django.conf.urls import patterns, url, include


urlpatterns = patterns('dashboard.views',
    url(r'^oneitem/(?P<id>\d+)/$', 'one_item', name='one_item'),
    url(r'^itemedit/(?P<id>\d+)/$', 'item_edit', name='edit item'),
    url(r'^itemslist/$', 'items_list', name='items list'),
)
