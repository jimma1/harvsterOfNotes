from django.shortcuts import render
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

from notes.models import Note
from notes.forms import NoteForm

# Create your views here.

def add_note(request):
	if request.method == 'POST':
		form = NoteForm(request.POST)
		if form.is_valid():
			form.save()
			messages.add_message(request, messages.INFO, 'Note Added')
			return HttpResponseRedirect(reverse('notes:index'))
	else:
		form = NoteForm()
		context = {'form': form}
	return render(request, 'notes/addnote.html', context)

def index_view(request):
	notes = Note.objects.all()
	context = {}
	return render (request, 'notes/index.html', {'notes': notes})
