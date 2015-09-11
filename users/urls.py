from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from users import views


# API endpoints
urlpatterns = format_suffix_patterns([
    url(r'^$', views.api_root),
    url(r'^users/$', views.UserList.as_view(), name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(), name='user-detail'),

    url(r'^points-ranking/$', views.RankingPointList.as_view(), name='ranking-point-list'),
    url(r'^levels-ranking/$', views.RankingLevelList.as_view(), name='ranking-level-list'),

    url(r'^levels-golden-ranking/$', views.RankingGoldenList.as_view(), name='ranking-golden-list'),
    url(r'^levels-silver-ranking/$', views.RankingSilverList.as_view(), name='ranking-silver-list'),
    url(r'^levels-bronze-ranking/$', views.RankingBronzeList.as_view(), name='ranking-bronze-list'),

    url(r'^actions/$', views.ActionList.as_view(), name='action-list'),
    url(r'^actions/(?P<pk>[0-9]+)/$', views.ActionDetail.as_view(), name='action-detail'),


    #probando:
    #url(r'^users_actions/(?P<pk>[0-9]+)/$', views.UserAction.as_view(), name='user-action'),
    url(r'^users/(?P<pk>[0-9]+)/actions/(?P<pk2>[0-9]+)/$', views.UserAction.as_view(), name='user-action'),

# Login and logout views for the browsable API
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
])
