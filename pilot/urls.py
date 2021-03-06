"""pilot URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
#TODO Add url mapping to each of the apps. and create a urls.py for each of them
    url(r'^$', include('home.urls'), name='home'),
  #  url(r'', include('gcm.urls')),
	url(r'^admin/', admin.site.urls),
	url(r'^form/',include('form.urls'), name='form'),
    url(r'^home/',include('home.urls'), name='home'),
    url(r'^messaging/', include('messaging.urls'), name='messaging'),
    url(r'^analyse/',include('analyse.urls'), name='analyse'),
    url(r'^userAdmin/',include('userAdmin.urls'), name='userAdmin'),
  #  url(r'^favicon.ico$', django.views.static.serve, {'/': '/favicon.ico'}),
]
