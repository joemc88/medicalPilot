from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from django.contrib.auth.views import logout
from django.contrib.auth import authenticate, login
from userAdmin.models import Patient, Doctor
from form.models import FormSubmission, LBPCharacterise, PainPerceptionDiary, BackPain
import datetime
def index(request ):
	return render(request, 'analyse/index.html',)


def ppd(request):
	#show graph page without the actual graph, just includes a drop down to choose patient and parameter.
	Patients = Patient.objects.filter(primary_physician =   request.user.id)
	context = {'patients':Patients}
	return render(request, 'analyse/graph.html', context)

#these methods call ppdGraphRender with a specific parameter and patient
def ppdPainAtWorst(request, patient_id):
	return ppdRenderGraph(request, patient_id, 'painAtWorst')

def ppdPainAtLeast(request, patient_id):
	return ppdRenderGraph(request, patient_id, 'painAtLeast')

def ppdPainOnAverage(request, patient_id):
	return ppdRenderGraph(request, patient_id, 'painOnAverage')

def ppdPainRightNow(request, patient_id):
	return ppdRenderGraph(request, patient_id, 'painRightNow')

def ppdGeneralActivity(request, patient_id):
	return ppdRenderGraph(request, patient_id, 'generalActivity')

def ppdMood(request, patient_id):
	return ppdRenderGraph(request, patient_id, 'mood')

def ppdWalkingAbility(request, patient_id):
	return ppdRenderGraph(request, patient_id, 'walkingAbility')

def ppdNormalWork(request, patient_id):
	return ppdRenderGraph(request, patient_id, 'normalWork')

def ppdRelationships(request, patient_id):
	return ppdRenderGraph(request, patient_id, 'relationships')

def ppdSleep(request, patient_id):
	return ppdRenderGraph(request, patient_id, 'sleep')

def ppdEnjoyment(request, patient_id):
	return ppdRenderGraph(request, patient_id, 'enjoyment')



def ppdRenderGraph(request, patient_id, requestedData):
	#logic for extracting relevant data from DB and passing it to page which links to chart.js to render graph
	Patients = Patient.objects.filter(primary_physician =   request.user.id)
	selectedPatient = Patient.objects.get(id  = patient_id)
	PainDiaries = PainPerceptionDiary.objects.filter(patient = patient_id)
	dates = []
	values = []
	for i in PainDiaries:
		dates.append(i.date.strftime("%Y-%m-%d %H:%M"))
		values.append(dataPicker(i, requestedData))
	context = {'dates': dates, 'values':values, 'patients':Patients, 'selectedPatient': selectedPatient, 'requestedData':requestedData}

	return render(request, 'analyse/graph.html',context)

def dataPicker(record, requestedData):
	return {
		'painAtWorst': record.PainAtWorst,
		'painAtLeast': record.PainAtLeast,
		'painOnAverage': record.PainOnAverage,
		'painRightNow': record.PainRightNow,
		'generalActivity': record.GeneralActivity,
        'mood': record.Mood,
        'walkingAbility': record.WalkingAbility,
        'normalWork': record.NormalWork,
        'relationships': record.Relationships,
        'sleep': record.Sleep,
        'enjoyment': record.EnjoymentOfLife
    }[requestedData]


def ppdAnalyseQueryHandler(request):
	return redirect('/analyse/ppd/'+request.POST.get("parameter", "")+'/'+request.POST.get("patient", ""))



