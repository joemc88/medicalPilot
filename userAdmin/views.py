from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404, HttpResponse
from django.contrib.auth.views import logout
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import Patient,Doctor,Nurse

def index(request):
	return render(request, "userAdmin/index.html")

# Create your views here.
def loginForm(request):
	return render(request, 'userAdmin/loginForm.html')

def auth_login(request):
	username = request.POST.get('username','')
	password = request.POST.get('password','')
	user = authenticate(request, username=username, password=password)
	if user is not None:
		login(request, user)
		# Redirect to a success page.
		return redirect('/')
	else:
		return HttpResponse("<p>Failed to log in. Incorrect username or password. <a href='/userAdmin/loginForm'>Try Again.</a></p>")

def auth_logout(request):
	logout(request)
	return redirect("/")

def createPatient(request):
	context ={
		'doctors' : Doctor.objects.all()
	}
	
	return render(request, 'userAdmin/createPatient.html',context)

def browsePatients(request):
	return HttpResponse("<h1>list of patients</h1>")

def submitNewPatient(request):
	#TODO make sure newly created users have the correct permissions to write to form submissions, messages etc
	username = request.POST.get('username','')
	email = request.POST.get('email','')
	password = request.POST.get('password1','')
	newUser = User.objects.create_user(username, email, password)
	newUser.first_name = request.POST.get('first_name','')
	newUser.last_name = request.POST.get('last_name','')
	newUser.save()
	patient = Patient.objects.create()
	patient.user = newUser
	patient.medical_card_number = request.POST.get('medical_card_number','')
	patient.date_of_birth = request.POST.get('date_of_birth','')
	patient.date_admitted = request.POST.get('date_admitted','')
	x = request.POST.get('physician','')
	patient.primary_physician = User.objects.get(id=x)
	patient.address_line_one = request.POST.get('address_line_one','')
	patient.address_line_two = request.POST.get('address_line_two','')
	patient.address_line_three = request.POST.get('address_line_two','')
	patient.save()
	return redirect("/")