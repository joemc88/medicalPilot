from django.db import models
from userAdmin.models import Patient ,Doctor
from django.contrib.auth.models import User

#class HospitalAdmin(models.Model):

#TODO clarify that this is the pain form. Allow for other forms, different table for each form, homepage of form app should show list of forms
class FormSubmission(models.Model):
	patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
	date = models.DateTimeField(auto_now_add=True )
	had_pain = models.CharField(max_length =250)
	when_started = models.CharField(max_length =250)
	where_pain = models.CharField(max_length =250)
	pain_frequency = models.CharField(max_length =250)
	pain_duration = models.CharField(max_length =250)
	medication = models.CharField(max_length =250)
	medication_works = models.CharField(max_length =250)
	life_disturbance = models.CharField(max_length =250)
	sleep_disturbed = models.CharField(max_length =250)

	def __str__(self):
		return "Template Pain Form: "+self.date.strftime("%d, %m, %Y")

class PainPerceptionDiary(models.Model):
	patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
	date = models.DateTimeField(auto_now_add=True )
	PainAtWorst = models.IntegerField()
	PainAtLeast = models.IntegerField()
	PainOnAverage = models.IntegerField()
	PainRightNow = models.IntegerField()
	GeneralActivity = models.IntegerField()
	Mood = models.IntegerField()
	WalkingAbility = models.IntegerField()
	NormalWork = models.IntegerField()
	Relationships = models.IntegerField()
	Sleep = models.IntegerField()
	EnjoymentOfLife = models.IntegerField()

	def __str__(self):
		return "Pain Perception Diary: "+self.date.strftime("%d, %m, %Y")

class LBPCharacterise(models.Model):
	patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
	date = models.DateTimeField(auto_now_add=True )

	Location =  models.CharField(max_length =250)
	Radiation = models.CharField(max_length =250)
	Duration = models.CharField(max_length =250)
	Periodicity = models.CharField(max_length =250)
	Character =  models.CharField(max_length =250)
	AggrivatingFactors = models.CharField(max_length =250)
	RelievingFactors =  models.CharField(max_length =250)
	ASNumbness = models.BooleanField()
	ASParaesthesia = models.BooleanField()
	ASSyncope = models.BooleanField()
	ASWeakness = models.BooleanField()
	ASSphincterDisturbance = models.BooleanField()
	ASDizziness = models.BooleanField()
	ASOther = models.BooleanField()
	ASOtherStated = models.CharField(max_length =250)
	Interventions_Analgesia = models.CharField(max_length =250)

	def __str__(self):
		return "LBP Charactarise: "+self.date.strftime("%B, %d, %Y")

class BackPain(models.Model):
	patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
	date = models.DateTimeField(auto_now_add=True )
	carriedOutBy = models.ForeignKey(User, null=True, related_name='backpainInspector')
	Inspection= models.CharField(max_length =250)
	Palpatation = models.CharField(max_length =250)
	Range_PainOnMovement = models.CharField(max_length =250)
	SLR_Right = models.CharField(max_length =250)
	Tone_Left = models.CharField(max_length =250)
	Tone_Right = models.CharField(max_length =250)
	Hip_Flexion_Left = models.CharField(max_length =250)
	Hip_Flexion_Right = models.CharField(max_length =250)

	Knee_Extension_Left = models.CharField(max_length =250)
	Knee_Extension_Right = models.CharField(max_length =250)

	Knee_Flexion_Left = models.CharField(max_length =250)
	Knee_Flexion_Right = models.CharField(max_length =250)
	Ankle_Dorsi_Flexion_Left = models.CharField(max_length =250)
	Ankle_Dorsi_Flexion_Right = models.CharField(max_length =250)
	Ankle_Plantar_Flexion_Left = models.CharField(max_length =250)
	Ankle_Plantar_Flexion_Right  = models.CharField(max_length =250)
	Extension_Hallicus_Longus_Left = models.CharField(max_length =250)
	Extension_Hallicus_Longus_Right = models.CharField(max_length =250)
	Coordination_Left = models.CharField(max_length =250)
	Coordination_Right = models.CharField(max_length =250)

	Sensation = models.CharField(max_length =250)

	Reflex_Knee_Left = models.CharField(max_length =250)
	Reflex_Knee_Right = models.CharField(max_length =250)
	Reflex_Ankle_Left = models.CharField(max_length =250)
	Reflex_Ankle_Right = models.CharField(max_length =250)
	Reflex_Plantar_Left = models.CharField(max_length =250)
	Reflex_Plantar_Right = models.CharField(max_length =250)

	def __str__(self):
		return "Back pain: "+self.date.strftime("%B, %d, %Y")







