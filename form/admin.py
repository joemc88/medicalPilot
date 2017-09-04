from django.contrib import admin

# Register your models here.
from .models import  FormSubmission, PainPerceptionDiary, LBPCharacterise, BackPain

admin.site.register(FormSubmission)
admin.site.register(PainPerceptionDiary)
admin.site.register(LBPCharacterise)

admin.site.register(BackPain)

