'''
Added this view so that the core part of the project handels the home part of site
'''
from django.shortcuts import render

from notes.models import Note

def home_view(request):
	notes = Note.objects.all().order_by('-timestamp')
	context = {'notes': notes}
	return render(request, 'home.html', context)