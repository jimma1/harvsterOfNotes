from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.utils.text import slugify
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
#from django.contrib.auth.models import User
#from django.contrib.auth import get_user

from notes.models import Note, Tag
from notes.forms import NoteForm, TagForm
from useraccounts.models import Member

# Create your views here.
'''
Code is repeated in add_tagg and add_note, and pagination is repeated two places. One other solution for this is to write class based views.
Since there is just this block which is repeated I do not prioritize to learn class based views now.
'''

def tag_search(request, **kwargs):
	slug = kwargs['slug']
	tag = get_object_or_404(Tag, slug=slug)
	notes = tag.notes.all()
	# pagination
	page_number = request.GET.get('page')
	paginator = Paginator(notes, 5)
	try:
		notes = paginator.page(page_number)
	except PageNotAnInteger:
		notes = paginator.page(1)
	except EmptyPage:
		notes = paginator.page(paginator.num_pages)
	
	context = {
		'notes': notes,
		'tag': tag}

	return render(request, 'notes/tagsearch.html', context)

def add_tag(request):
	#fetch tag by id to manipulate posted notes and pass the instance of posted note to form
	id = request.GET.get('id', None)
	if id is not None:
		tag = get_object_or_404(Tag, id=id)
	else:
		tag = None

	if request.method == 'POST':
		# delete tag
		if request.POST.get('control') == 'delete':
			tag.delete()
			messages.add_message(request, messages.INFO, 'Tag Deleted!')
			return HttpResponseRedirect(reverse('notes:index'))
		# new tag which is slugifyed by Django, due to url search on tags
		form = TagForm(request.POST, instance=tag)
		if form.is_valid():
			t = form.save(commit=False)
			t.slug = slugify(t.label)
			t.save()
			messages.add_message(request, messages.INFO, 'Tag Added')
			return HttpResponseRedirect(reverse('notes:index'))
	else:
		form = TagForm(instance=tag)
		context = {
			'form': form,
		 	'tag': tag
		 	}

	return render(request, 'notes/addtag.html', context)

def add_note(request):
	#fetch note by id to manipulate posted notes and pass the instance of posted note to form
	id = request.GET.get('id', None)
	if id is not None:
		note = get_object_or_404(Note, id=id)
	else:
		note = None

	# get the logged in user
	author = request.user

	if request.method == 'POST':
		# delete note
		if request.POST.get('control') == 'delete':
			note.delete()
			messages.add_message(request, messages.INFO, 'Note Deleted!')
			return HttpResponseRedirect(reverse('notes:index'))
		
		# new note
		form = NoteForm(request.POST, instance=note)
		if form.is_valid():
			# don't send form to DB yet
			new_author = form.save(commit=False)
			# add author
			new_author.author = author
			# send it to DB
			new_author.save()
			messages.add_message(request, messages.INFO, 'Note Added')
			return HttpResponseRedirect(reverse('notes:index'))
	else:
		form = NoteForm(instance=note)
		context = {
			'form': form,
		 	'note': note
		 	}

	return render(request, 'notes/addnote.html', context)

def index_view(request):
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

	if request.user.is_authenticated():
		user = request.user


	tags = Tag.objects.all()
	context = {
		'notes': notes,
		'tags': tags
		}
	return render (request, 'notes/index.html', context)
