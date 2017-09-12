#userAdmin urls


from . import views
from django.conf.urls import include, url
app_name = 'userAdmin'
#'^$' means default homepage within this 'app' or section of the website

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^loginForm/$', views.loginForm, name='loginForm'),
    url(r'^login/$', views.auth_login, name='auth_login'),
    url(r'^logout/$', views.auth_logout, name='auth_logout'),
    url(r'^createPatient/$', views.createPatient, name='createPatient'),
    url(r'^browsePatients/$', views.browsePatients, name='browsePatients'),
    url(r'^managePatients/$', views.managePatients, name='managePatients'),
    url(r'^registerDevice/$', views.registerDevice, name='registerDevice'),
    url(r'^sendReminders/$', views.sendReminders, name='sendReminders'),

    url(r'^submitNewPatient/$', views.submitNewPatient, name='submitNewPatient'),
    

]