from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from infos import views

urlpatterns = [
	url(r'^infos/$', views.InfoList.as_view()),
	url(r'^infos/(?P<pk>[0-9]+)/$', views.InfoDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
