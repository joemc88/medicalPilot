from django.conf.urls import url
from . import views

app_name = 'form'
#'^$' means default homepage within this 'app' or section of the website

urlpatterns = [
  	url(r'^$', views.index, name='index'),
  	url(r'^selectForm/$', views.selectForm, name='selectForm'),

    url(r'^mySubmissions', views.mySubmissions, name='mySubmissions'),
    url(r'^browsePatients', views.browsePatients, name='browsePatients'),
    url(r'^browseForms', views.browseForms, name='browseForms'),
    url(r'^browseTemplateForms', views.browseTemplateForms, name='browseTemplateForms'),
  
    url(r'^patientSubmissions/(?P<patient_id>[0-9]+)/$', views.patientSubmissions, name='patientSubmissions'),
    url(r'^review/(?P<submission_id>[0-9]+)/$', views.review, name='review'),

    url(r'^submitPainForm/$', views.submitPainForm, name="submitPainForm"),
    url(r'^painForm/$', views.painForm, name="painForm"),
    url(r'^backPainForm/$', views.backPainForm, name="backPainForm"),

    url(r'^submitBackPain/$', views.submitBackPain, name="submitBackPain"),

    url(r'^painPerceptionDiaryForm/$', views.painPerceptionDiaryForm, name="painPerceptionDiaryForm"),
    url(r'^submitPainPerceptionDiary/$', views.submitPainPerceptionDiary, name="submitPainPerceptionDiary"),
    url(r'^LBPCharacteriseForm/$', views.LBPCharacteriseForm, name="LBPCharacteriseForm"),
    url(r'^submitLBPCharacterise/$', views.submitLBPCharacterise, name="submitLBPCharacterise"),





]