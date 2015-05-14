# Modelform interacts fast and easy with DB through defined models
from django import forms
from notes.models import Note

class NoteForm(forms.ModelForm):
	class Meta:
		model = Note
		fields = ('label', 'body')