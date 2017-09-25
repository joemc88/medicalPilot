from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404, HttpResponse
from django.contrib.auth.views import logout
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import Patient,Doctor,Administrator, PatientReminders
from gcm import *
import datetime

def index(request):
	print(request)
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
	physician = request.POST.get('physician','')

	patient = Patient.objects.create(
	user = newUser,
	medical_card_number = request.POST.get('medical_card_number',''),
	date_of_birth = request.POST.get('date_of_birth',''),
	date_admitted = request.POST.get('date_admitted',''),
	primary_physician = User.objects.get(id=physician),
	address_line_one = request.POST.get('address_line_one',''),
	address_line_two = request.POST.get('address_line_two',''),
	address_line_three = request.POST.get('address_line_two',''),
	submitsPainForm = request.POST.get('submitsPainForm', False),
	submitsPPD = request.POST.get('submitsPPD', False),
	submitsLBPCharacterise = request.POST.get('submitsLBPCharacterise', False),
	submitsBackPain = request.POST.get('submitsBackPain', False)
	)

	patient.save()

	if patient.submitsPainForm:
		#logic for making patient reminder
		PainFormReminder = PatientReminders.objects.create()
		PainFormReminder.patient = patient
		PainFormReminder.formType = "PainForm"
		PainFormReminder.submissionFrequency = request.POST.get('painFormNotify','Never')
		PainFormReminder.lastReminder = datetime.date.today()
		PainFormReminder.save()

	if patient.submitsLBPCharacterise:
		LBPCReminder = PatientReminders.objects.create()
		LBPCReminder.patient = patient
		LBPCReminder.formType = "LBPCharacterise"
		LBPCReminder.submissionFrequency = request.POST.get('lbpcNotify','Never')
		LBPCReminder.lastReminder = datetime.date.today()
		LBPCReminder.save()

	if patient.submitsPPD:
		PPDReminder = PatientReminders.objects.create()
		PPDReminder.patient = patient
		PPDReminder.formType = "PainPerceptionDiary"
		PPDReminder.submissionFrequency = request.POST.get('ppdNotify','Never')
		PPDReminder.lastReminder = datetime.date.today()
		PPDReminder.save()

	if patient.submitsBackPain:
		BackPainReminder = PatientReminders.objects.create()
		BackPainReminder.patient = patient
		BackPainReminder.formType = "BackPain"
		BackPainReminder.submissionFrequency = request.POST.get('backPainNotify','Never')
		BackPainReminder.lastReminder = datetime.date.today()
		BackPainReminder.save()

	return redirect("/userAdmin/managePatients/")

def managePatients(request):
	context ={'patients' : Patient.objects.all()}
	return render(request, 'userAdmin/managePatients.html',context)


def sendReminder(request):

	return redirect('/userAdmin/managePatients')


def registerDevice(request):
	print("arrived at register device")
	print(request.COOKIES.get("sessionid") )
	if request.user.is_authenticated():
		patient = Patient.objects.get(user = request.user)
		token =request.GET.get('token','')
		patient.deviceToken = token
		patient.save();
		
		return HttpResponse("success")
	else:
		return HttpResponse("failure")

def sendReminders(request):
	reminders = PatientReminders.objects.all()
 
	for reminder in reminders:
		timeElapsed = datetime.date.today() - reminder.lastReminder.date()
		print(timeElapsed)
		if  (reminder.submissionFrequency =='daily'):# and (timeElapsed < datetime.timedelta(days=1)):
			token = reminder.patient.deviceToken
			gcm = GCM("AAAA3EPwcVU:APA91bGQKwkhEKjWQf5CPAbVXXzhFTa5tpl6IJ2VYSAb5mbn2dBF5ppMUAKzm8OAKR4NRkX3x-Juyk9TBcqjKUmLxUWAXU33j_9KHCsyyIzaJ4up_2dhFxt1wkw9OthRXrXFob11QGPl")
			data = {'message': 'remember to submit your form'}
			gcm.plaintext_request(registration_id=token, data = data) 
			reminder.lastReminder = datetime.date.today()
			reminder.save()
		
		if  reminder.submissionFrequency =='weekly' and (timeElapsed >datetime.timedelta(days=7)):
			token = reminder.patient.deviceToken
			gcm = GCM("AAAA3EPwcVU:APA91bGQKwkhEKjWQf5CPAbVXXzhFTa5tpl6IJ2VYSAb5mbn2dBF5ppMUAKzm8OAKR4NRkX3x-Juyk9TBcqjKUmLxUWAXU33j_9KHCsyyIzaJ4up_2dhFxt1wkw9OthRXrXFob11QGPl")
			data = {'message': 'remember to submit your form'}
			gcm.plaintext_request(registration_id=token, data = data) 
			reminder.lastReminder = datetime.date.today()
			reminder.save()

		if  reminder.submissionFrequency =='monthly' and (timeElapsed >datetime.timedelta(days=30)):
			token = reminder.patient.deviceToken
			gcm = GCM("AAAA3EPwcVU:APA91bGQKwkhEKjWQf5CPAbVXXzhFTa5tpl6IJ2VYSAb5mbn2dBF5ppMUAKzm8OAKR4NRkX3x-Juyk9TBcqjKUmLxUWAXU33j_9KHCsyyIzaJ4up_2dhFxt1wkw9OthRXrXFob11QGPl")
			data = {'message': 'remember to submit your form'}
			gcm.plaintext_request(registration_id=token, data = data)
			reminder.lastReminder = datetime.date.today()
			reminder.save() 
	return redirect('/userAdmin')


