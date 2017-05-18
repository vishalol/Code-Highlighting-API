from django.conf.urls import url
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^snippetList/$', views.SnippetList.as_view(), name = 'snippetlist'),
    url(r'^snippetList/(?P<pk>[0-9]+)$', views.SnippetDetail.as_view(), name = 'snippetdetail'),
	url(r'^users/$', views.UserList.as_view(), name = 'userlist'),
	url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(), name = 'userdetail'),
	url(r'^$', views.api_root),
	url(r'^snippetList/(?P<pk>[0-9]+)/highlight/$', views.SnippetHighlight.as_view(), name = 'highlight'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
