from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm

from useraccounts.models import Member

class RegistrationForm(ModelForm):
	first_name = forms.CharField(label=(u'First Name'))
	last_name = forms.CharField(label=(u'Last Name'))
	username = forms.CharField(label=(u'Username'))
	email = forms.EmailField(label=(u'Email Address'))
	# wdiget render_vaule is false for hiding user input
	password = forms.CharField(label=(u'Password'), widget=forms.PasswordInput(render_value=False))
	password1 = forms.CharField(label=(u'Verify Password'), widget=forms.PasswordInput(render_value=False))

	class Meta:
		model = Member
		# do not import from model
		exclude = ('user',)

	# when called in view, check if username is taken
	def clean_username(self):
		# data coming back for the form after posting in view
		username= self.cleaned_data['username']
		try:
			User.objects.get(username=username)
		except User.DoesNotExist:
			return username
		raise forms.ValidationError("That username is occupied. Please choose another")

	# password check
	def clean(self):
		password = self.cleaned_data.get('password')
		password1 = self.cleaned_data.get('password1')
		if password != password1:
			raise forms.ValidationError("Passwords don't match. Try again")
		return self.cleaned_data



class LoginForm(forms.Form):
	username = forms.CharField(label=(u'Username'))
	password = forms.CharField(label=(u'Password'), widget=forms.PasswordInput(render_value=False))