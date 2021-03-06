from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from django.contrib.auth.views import logout
from django.contrib.auth import authenticate, login
from userAdmin.models import Patient, Doctor, Administrator
from gcm import *
def index(request):
	#if user is logged in, pass the type of user to index.html otherwise redirect to login page
	if request.user.is_authenticated():
		try:
			doctor = Doctor.objects.get(user = request.user)
			userIsDoctor = True
			pass
		except Doctor.DoesNotExist:
			userIsDoctor = False
		try:
			admin =  Administrator.objects.get(user = request.user)
			userIsAdmin = True
		except Administrator.DoesNotExist:
			userIsAdmin = False

		context = {'userIsDoctor': userIsDoctor, 'userIsAdmin': userIsAdmin }
		return render(request, 'home/index.html', context)
	else:
		return redirect('/userAdmin/loginForm/')
# Create your views here.
