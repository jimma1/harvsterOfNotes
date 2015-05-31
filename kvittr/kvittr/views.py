'''
Added this view so that the core part of the project handels the home part of site
'''
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from notes.models import Note, Tag

def home_view(request):
	notes = Note.objects.all().order_by('-timestamp')
	# Pagination
	page_number = request.GET.get('page')
	paginator = Paginator(notes, 5)
	try:
		notes = paginator.page(page_number)
	except PageNotAnInteger:
		notes = paginator.page(1)
	except EmptyPage:
		notes = paginator.page(paginator.num_pages)

	tags = Tag.objects.all().order_by('label')
	context = {
		'notes': notes,
		'tags': tags
		}
	return render(request, 'home.html', context)