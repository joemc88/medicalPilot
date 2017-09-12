from django.contrib import admin

# Register your models here.
from .models import  Patient, Doctor, Nurse, PatientReminders

admin.site.register(Patient)
admin.site.register(PatientReminders)

admin.site.register(Doctor)
admin.site.register(Nurse)
