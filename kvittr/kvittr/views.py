'''
Added this view so that the core part of the project handels the home part of site
'''
from django.shortcuts import render

def home_view(request):
	return render(request, 'home.html')