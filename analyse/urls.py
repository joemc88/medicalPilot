#analyse urls

from django.conf.urls import url
from . import views

app_name = 'analyse'


urlpatterns = [
	url(r'^$', views.index, name='index'),
]