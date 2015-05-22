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

	# email check
	def clean_email(self):
		email = self.cleaned_data['email']
		try:
			User.objects.get(email=email)
		except User.DoesNotExist:
			return email
		raise forms.ValidationError("That email is allready taken. Please use another email address")

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

class UserupdateForm(forms.ModelForm):
	first_name = forms.CharField(label=(u'First Name'), required=True)
	last_name = forms.CharField(label=(u'Last Name'), required=True)
	email = forms.EmailField(label=(u'Email Address'), required=True)

	class Meta:
		model = User
		fields = (
			'first_name',
			'last_name',
			'email'
			)

	def save(self, commit=True):
		user = super(UserupdateForm, self).save(commit=False)
		user.first_name = self.cleaned_data['first_name']
		user.last_name= self.cleaned_data['last_name']
		user.email = self.cleaned_data['email']

		if commit:
			user.save()

		return user