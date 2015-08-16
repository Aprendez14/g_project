"""
from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from users import views

urlpatterns = [
    url(r'^$', views.api_root),
    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
"""

from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from users import views


# API endpoints
urlpatterns = format_suffix_patterns([
    url(r'^$', views.api_root),
    url(r'^users/$',
        views.UserList.as_view(),
        name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)/$',
        views.UserDetail.as_view(),
        name='user-detail'),

    url(r'^ranking/$',
        views.RankingList.as_view(),
        name='ranking-list'),
])


# Login and logout views for the browsable API
urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]
