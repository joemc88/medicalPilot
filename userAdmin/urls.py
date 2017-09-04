#userAdmin urls

from django.conf.urls import url
from . import views

app_name = 'userAdmin'
#'^$' means default homepage within this 'app' or section of the website

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^loginForm/$', views.loginForm, name='loginForm'),
    url(r'^login/$', views.auth_login, name='auth_login'),
    url(r'^logout/$', views.auth_logout, name='auth_logout'),
    url(r'^createPatient/$', views.createPatient, name='createPatient'),
    url(r'^browsePatients/$', views.browsePatients, name='browsePatients'),
    url(r'^submitNewPatient/$', views.submitNewPatient, name='submitNewPatient'),
    

]