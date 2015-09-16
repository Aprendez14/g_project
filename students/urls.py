from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from students import views


# API endpoints
urlpatterns = format_suffix_patterns([
    url(r'^$', views.api_root),
    url(r'^students/$', views.StudentList.as_view(), name='student-list'),
    url(r'^students/(?P<pk>[0-9]+)/$', views.StudentDetail.as_view(), name='student-detail'),

    url(r'^point-ranking/$', views.RankingPointList.as_view(), name='ranking-point-list'),
    url(r'^level-ranking/$', views.RankingLevelList.as_view(), name='ranking-level-list'),

    url(r'^golden-ranking/$', views.RankingGoldenList.as_view(), name='ranking-golden-list'),
    url(r'^silver-ranking/$', views.RankingSilverList.as_view(), name='ranking-silver-list'),
    url(r'^bronze-ranking/$', views.RankingBronzeList.as_view(), name='ranking-bronze-list'),

    url(r'^actions/$', views.ActionList.as_view(), name='action-list'),
    url(r'^actions/(?P<pk>[0-9]+)/$', views.ActionDetail.as_view(), name='action-detail'),


    #probando:
    #url(r'^students_actions/(?P<pk>[0-9]+)/$', views.StudentAction.as_view(), name='student-action'),
    url(r'^students/(?P<pk>[0-9]+)/actions/(?P<pk2>[0-9]+)/$', views.StudentAction.as_view(), name='student-action'),

# Login and logout views for the browsable API
    #url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
])
