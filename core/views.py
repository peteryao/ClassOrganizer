from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Permission
from django.contrib.auth.decorators import login_required, permission_required

def index(request):
	context = {}
	
	return render(request, 'core/index.html', context)
