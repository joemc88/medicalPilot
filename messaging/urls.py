#messaging urls

from django.conf.urls import url
from . import views

app_name = 'messaging'
#'^$' means default homepage within this 'app' or section of the website

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^newMessage/$', views.messageForm, name='messageForm'),
url(r'^sendMessage/$', views.sendMessage, name='sendMessage'),
url(r'^sendReply/$', views.sendReply, name='sendReply'),

url(r'^conversation/(?P<conversation_id>[0-9]+)/$', views.conversation, name='conversation'),

    
]