from django.db import models

# Create your models here.
from django.contrib.auth.models import User
# Create your models here.

class Patient(models.Model):
	user = models.ForeignKey(User, null=True, related_name='patient_user')
	medical_card_number = models.CharField(max_length=100)
	date_of_birth = models.CharField(max_length=100)
	date_admitted = models.CharField(max_length=100)
	primary_physician = models.ForeignKey(User, null=True, related_name='primary_physician')
	deviceToken = models.CharField(max_length=1000, null=True)
	address_line_one = models.CharField(max_length=100)
	address_line_two = models.CharField(max_length=100)
	address_line_three = models.CharField(max_length=100)
	submitsPainForm = models.BooleanField()	
	submitsPPD = models.BooleanField()	
	submitsBackPain = models.BooleanField()
	submitsLBPCharacterise = models.BooleanField()
	
	def __str__(self):
		
		return self.user.first_name + " " +self.user.last_name + "\n Medical Card: "+  self.medical_card_number +"\n" + "\n DOB: "+ self.date_of_birth +"\n"

class PatientReminders(models.Model):
	patient = models.ForeignKey(Patient, null=True, related_name='reminder_patient')
	formType = models.CharField(max_length=50)
	submissionFrequency = models.CharField(max_length=20)
	lastReminder = models.DateTimeField(auto_now_add=True )



class Doctor(models.Model):
	user = models.ForeignKey(User, null=True, related_name='doctor_user')
	phone_number = models.CharField(max_length=15)
	specialty = models.CharField(max_length=50)

	def __str__(self):
		#return str(self.user)
		return self.user.first_name + " " +self.user.last_name + "\n Specialty: "+ self.specialty +"\n"

class Administrator(models.Model):
	user = models.ForeignKey(User, null=True, related_name='nurse_user')
	phone_number = models.CharField(max_length=15)

	def __str__(self):
		
		return "Admin "+self.user.first_name + " " +self.user.last_name+"\n"