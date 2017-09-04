from django.http import HttpResponse
from userAdmin.models import Patient, Doctor
from .models import FormSubmission, LBPCharacterise, PainPerceptionDiary, BackPain
from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from django.contrib.auth.views import logout
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


import datetime

def index(request):
	if request.user.is_authenticated():
		try:
			doctor = Doctor.objects.get(user = request.user)
			isDoctor = True
		except Doctor.DoesNotExist:
			isDoctor = False
		context = {'isDoctor': isDoctor}
		return render(request, 'form/index.html', context)
	else:
		return redirect('/userAdmin/loginForm')

def selectForm(request):
	#TODO each patient model should reflect excacly which forms they are expected to submit.
	#for now just assume all 
	#TODO add feature to highlight which forms are due
	context = {'painForm':True}
	return render(request, 'form/selectForm.html', context)

def mySubmissions(request):

	painForms = FormSubmission.objects.filter(patient =Patient.objects.get(user = request.user.id) )
	painDiaries = PainPerceptionDiary.objects.filter(patient =Patient.objects.get(user = request.user.id))
	LBPs = LBPCharacterise.objects.filter(patient=Patient.objects.get(user = request.user.id) )
	BackPains = BackPain.objects.filter(patient=Patient.objects.get(user = request.user.id) )
	context ={
		'patient' : Patient.objects.get(user = request.user.id),
		'painForms' : painForms,
		'painDiaries': painDiaries,
		'LBPs': LBPs,
		'BackPains' : BackPains,
		
	}
	return render(request, 'form/submissions.html', context)


def patientSubmissions(request, patient_id):
	#TODO fix is doctor check. dont limit to pain form submissions
	painForms = FormSubmission.objects.filter(patient = patient_id) 
	painDiaries = PainPerceptionDiary.objects.filter(patient =patient_id)
	LBPs = LBPCharacterise.objects.filter(patient=patient_id) 
	BackPains = BackPain.objects.filter(patient = patient_id) 
	context ={
		'patient' : Patient.objects.get(id = patient_id),
		'painForms' : painForms,
		'painDiaries': painDiaries,
		'LBPs': LBPs,
		'BackPains' : BackPains,
		
	}
	return render(request, 'form/submissions.html', context)	


def review(request, submission_id):
	
	submission = get_object_or_404(FormSubmission, id = submission_id)
	context = {
		'patient':submission.patient,
		'submission':submission
	}

	return render(request, 'form/review.html', context)
	

def painForm(request):
	context = {
	 'user': request.user,
	 'date': datetime.date.today()

	}
	return render(request, 'form/painForm.html',context)

def backPainForm(request):
	return HttpResponse("backpainform")

def submitBackPain(request):
	return HttpResponse("submit back pain")
#prototype for submitting new form
def submitPainForm(request):
	patient = Patient.objects.get(user = request.user.id)
	patient.formsubmission_set.create(
		date = datetime.date.today(),
		had_pain =request.POST.get("had_pain", ""),
		when_started =request.POST.get("when_started", ""),
		where_pain = request.POST.get("where_pain", ""),
		pain_frequency = request.POST.get("pain_frequency", ""),
		pain_duration = request.POST.get("pain_duration", ""),
		medication =  request.POST.get("medication", ""),
		medication_works = request.POST.get("medication_works", ""),
		life_disturbance = request.POST.get("life_disturbance", ""),
		sleep_disturbed = request.POST.get("sleep_disturbed", "")
	)
	return redirect('/form/mySubmissions')


def browsePatients(request):
	try:
		doctor = Doctor.objects.get(user = request.user)
		try:
			patients = Patient.objects.filter(primary_physician = request.user)
			context ={'patients': patients}
			return render(request, 'form/browsePatients.html',context)
		except Patient.DoesNotExist:
			return HttpResponse("you have no patients")
	except Doctor.DoesNotExist:
		return HttpResponse("you are not a doctor. Access Denied")

def browseForms(request):
		return render(request, 'form/browseForms.html')

def browseTemplateForms(request):
	#logic for getting all template pain forms submitted by patients where user is their primary physician
	submissions = FormSubmission.objects.filter(patient = Patient.objects.filter(primary_physician = request.user))
	context ={'submissions':submissions}
	return render(request, 'form/browseTemplateForms.html',context)

def painPerceptionDiaryForm(request):
	context = {
	 'user': request.user,
	 'date': datetime.date.today()

	}
	return render(request, 'form/painPerceptionDiary.html', context)


def submitPainPerceptionDiary(request):
	patient = Patient.objects.get(user = request.user.id)
	patient.painperceptiondiary_set.create(
		date =datetime.date.today(),
		PainAtWorst =request.POST.get("PainAtWorst", ""),
		PainAtLeast =request.POST.get("PainAtLeast", ""),
		PainOnAverage = request.POST.get("PainOnAverage", ""),
		PainRightNow = request.POST.get("PainRightNow", ""),
	

		GeneralActivity = request.POST.get("GeneralActivity", ""),
		Mood =  request.POST.get("Mood", ""),
		WalkingAbility = request.POST.get("WalkingAbility", ""),
		NormalWork = request.POST.get("NormalWork", ""),
	
		EnjoymentOfLife = request.POST.get("EnjoymentOfLife", ""),
		Relationships = request.POST.get("Relationships", ""),
		Sleep = request.POST.get("Sleep", "")

	)
	return redirect('/form/mySubmissions')

def LBPCharacteriseForm(request):
	context = {
	 'user': request.user,
	 'date': datetime.date.today()

	}
	return render(request, 'form/LBPCharacterise.html', context)	


def submitLBPCharacterise(request):
	patient = Patient.objects.get(user = request.user.id)
	patient.lbpcharacterise_set.create(
		date =datetime.date.today(),
		Location =request.POST.get("Location", ""),
		Radiation =request.POST.get("Radiation", ""),
		Duration = request.POST.get("Duration", ""),
		Periodicity = request.POST.get("Periodicity", ""),
	
		Character = request.POST.get("Character", ""),
		AggrivatingFactors =  request.POST.get("AggrivatingFactors", ""),
		RelievingFactors = request.POST.get("RelievingFactors", ""),
		ASNumbness = request.POST.get("AsNumbness", False),
	
		ASParaesthesia = request.POST.get("ASParaesthesia", False),
		ASSyncope = request.POST.get("ASSyncope", False),
		ASWeakness = request.POST.get("ASWeakness", False),
		ASSphincterDisturbance = request.POST.get("ASSphincterDisturbance", False),

		ASDizziness = request.POST.get("ASDizziness", False),
		ASOther = request.POST.get("ASOther", False),
		ASOtherStated = request.POST.get("ASOtherStated", "")
	)
	return redirect('/form/mySubmissions')
