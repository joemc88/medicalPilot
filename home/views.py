from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from django.contrib.auth.views import logout
from django.contrib.auth import authenticate, login
from userAdmin.models import Patient, Doctor
def index(request):
	if request.user.is_authenticated():
		try:
			doctor = Doctor.objects.get(user = request.user)
			userIsAdmin = True
			pass
		except Doctor.DoesNotExist:
			userIsAdmin = False
		


		context = {'userIsAdmin': userIsAdmin }
		return render(request, 'home/index.html', context)
	else:
		return redirect('/userAdmin/loginForm/')
# Create your views here.
