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
    url(r'^browsePainSubmissions', views.browsePainSubmissions, name='browsePainSubmissions'),
    url(r'^browseBackPainSubmissions', views.browseBackPainSubmissions, name='browseBackPainSubmissions'),
    url(r'^browsePainPerceptionDiarySubmissions', views.browsePainPerceptionDiarySubmissions, name='browsePainPerceptionDiarySubmissions'),

    url(r'^browseLBPCharacteriseSubmissions', views.browseLBPCharacteriseSubmissions, name='browseLBPCharacteriseSubmissions'),

  
    url(r'^patientSubmissions/(?P<patient_id>[0-9]+)/$', views.patientSubmissions, name='patientSubmissions'),
    url(r'^reviewPainSubmission/(?P<submission_id>[0-9]+)/$', views.reviewPainSubmission, name='reviewPainSubmission'),
    url(r'^reviewPainPerceptionDiarySubmission/(?P<submission_id>[0-9]+)/$', views.reviewPainPerceptionDiarySubmission, name='reviewPainPerceptionDiarySubmission'),
    url(r'^reviewBackPainSubmission/(?P<submission_id>[0-9]+)/$', views.reviewBackPainSubmission, name='reviewBackPainSubmission'),
    url(r'^reviewLBPCharacteriseSubmission/(?P<submission_id>[0-9]+)/$', views.reviewLBPCharacteriseSubmission, name='reviewLBPCharacteriseSubmission'),


    url(r'^submitPainForm/$', views.submitPainForm, name="submitPainForm"),
    url(r'^painForm/$', views.painForm, name="painForm"),
    url(r'^backPainForm/$', views.backPainForm, name="backPainForm"),

    url(r'^submitBackPain/$', views.submitBackPain, name="submitBackPain"),

    url(r'^painPerceptionDiaryForm/$', views.painPerceptionDiaryForm, name="painPerceptionDiaryForm"),
    url(r'^submitPainPerceptionDiary/$', views.submitPainPerceptionDiary, name="submitPainPerceptionDiary"),
    url(r'^LBPCharacteriseForm/$', views.LBPCharacteriseForm, name="LBPCharacteriseForm"),
    url(r'^submitLBPCharacterise/$', views.submitLBPCharacterise, name="submitLBPCharacterise"),





]