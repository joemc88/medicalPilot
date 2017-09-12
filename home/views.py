from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from django.contrib.auth.views import logout
from django.contrib.auth import authenticate, login
from userAdmin.models import Patient, Doctor
from gcm import *
def index(request):
	#gcm = GCM("AAAA3EPwcVU:APA91bGQKwkhEKjWQf5CPAbVXXzhFTa5tpl6IJ2VYSAb5mbn2dBF5ppMUAKzm8OAKR4NRkX3x-Juyk9TBcqjKUmLxUWAXU33j_9KHCsyyIzaJ4up_2dhFxt1wkw9OthRXrXFob11QGPl")
	#data = {'message': 'Remember to submit your pain form.'}

	#reg_id = 'dSUuoNROjWA:APA91bFJ2HEUX6KrN2F003k-tQyWp1WmfUnGxarVTZ4eopJrIXtrYnBgpN2c_1GbsKfTeLMg_uKCzKEQHPBl4SHOdkWoyAXjkteKqaFEncFsuGJYNScsC6_uAHpSw5o9ihdx_oSHp3m6'

	#gcm.plaintext_request(registration_id=reg_id, data=data)






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
