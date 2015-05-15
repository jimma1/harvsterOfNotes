from django import forms

from useraccounts.models import Member

class LoginForm(forms.Form):
	username = forms.CharField(label=(u'Username'))
	password = forms.CharField(label=(u'Password'), widget=forms.PasswordInput(render_value=False))