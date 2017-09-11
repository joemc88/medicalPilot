#analyse urls

from django.conf.urls import url
from . import views

app_name = 'analyse'


urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^ppd/$', views.ppd, name='ppd'),
	url(r'^ppdAnalyseQueryHandler/$', views.ppdAnalyseQueryHandler, name='ppdAnalyseQueryHandler'),



	url(r'^ppd/painAtWorst/(?P<patient_id>[0-9]+)/$', views.ppdPainAtWorst, name='ppdPainAtWorst'),
	
	url(r'^ppd/painAtLeast/(?P<patient_id>[0-9]+)/$', views.ppdPainAtLeast, name='ppdPainAtLeast'),

	url(r'^ppd/painOnAverage/(?P<patient_id>[0-9]+)/$', views.ppdPainOnAverage, name='ppdPainOnAverage'),

	url(r'^ppd/painRightNow/(?P<patient_id>[0-9]+)/$', views.ppdPainRightNow, name='ppdPainRightNow'),

	url(r'^ppd/generalActivity/(?P<patient_id>[0-9]+)/$', views.ppdGeneralActivity, name='ppdGeneralActivity'),

	url(r'^ppd/mood/(?P<patient_id>[0-9]+)/$', views.ppdMood, name='ppdMood'),

	url(r'^ppd/walkingAbility/(?P<patient_id>[0-9]+)/$', views.ppdWalkingAbility, name='ppdWalkingAbility'),

	url(r'^ppd/normalWork/(?P<patient_id>[0-9]+)/$', views.ppdNormalWork, name='ppdNormalWork'),

	url(r'^ppd/relationships/(?P<patient_id>[0-9]+)/$', views.ppdRelationships, name='ppdRelationships'),

	url(r'^ppd/sleep/(?P<patient_id>[0-9]+)/$', views.ppdSleep, name='ppdSleep'),

	url(r'^ppd/enjoyment/(?P<patient_id>[0-9]+)/$', views.ppdEnjoyment, name='ppdEnjoyment'),

#	url(r'^painDiaries/(?P<patient_id>[0-9]+)/$', views.index, name='index')

]