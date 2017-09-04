from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from django.contrib.auth.views import logout
from django.contrib.auth import authenticate, login

def index(request):
	return HttpResponse("<h1>analysis homePage</h1>")

# Create your views here.

# Create your views here.
