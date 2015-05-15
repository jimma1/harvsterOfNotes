from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

from notes.models import Note, Tag
from notes.forms import NoteForm, TagForm

# Create your views here.
'''
Code is repeated in add_tagg and add_note. One other solution for this is to write class based views.
Since there is just this block which is repeated I do not prioritize to learn class based views now.
'''

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
		# new tag
		form = TagForm(request.POST, instance=tag)
		if form.is_valid():
			form.save()
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

	if request.method == 'POST':
		# delete note
		if request.POST.get('control') == 'delete':
			note.delete()
			messages.add_message(request, messages.INFO, 'Note Deleted!')
			return HttpResponseRedirect(reverse('notes:index'))
		# new note
		form = NoteForm(request.POST, instance=note)
		if form.is_valid():
			form.save()
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
	tags = Tag.objects.all()
	context = {
		'notes': notes,
		'tags': tags
		}
	return render (request, 'notes/index.html', context)
