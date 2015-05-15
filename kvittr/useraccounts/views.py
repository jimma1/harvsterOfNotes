from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from useraccounts.forms import LoginForm, RegistrationForm

# Create your views here.

def user_registration(request):
	if request.method == 'POST':
		# get userinput in form
		form = RegistrationForm(request.POST)
		# check with forms method before creating user object
		if form.is_valid():
			user = User.objects.create_user(
				username=form.cleaned_data['username'],
				email=form.cleaned_data['email'],
				first_name=form.cleaned_data['first_name'],
				last_name=form.cleaned_data['last_name'],
				password=form.cleaned_data['password']
				)
			user.save()
			return HttpResponseRedirect(reverse('notes:index'))
		# not valid
		else:
			context = {'form': form}
			return render(request, 'useraccounts/registration.html', context)
	# not post
	else:
		form = RegistrationForm()
		context = {'form': form}
		return render(request, 'useraccounts/registration.html', context)

def user_logut(request):
	logout(request)
	return redirect('home')

def user_login(request):
	if request.method == 'POST':
		# fetch filled out form
		form = LoginForm(request.POST)
		if form.is_valid():
			# ecstract userinfo from form
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			# authenticate
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				return HttpResponseRedirect(reverse('notes:index'))
			# is none
			else:
				context = {'form': form}
				return render (request, 'useraccounts/login.html', context)
		# not valid
		else:
			context = {'form': form}
			return render (request, 'useraccounts/login.html', context)
	# if not post show blank form
	else:
		form = LoginForm()
		context = {'form': form}
		return render (request, 'useraccounts/login.html', context)
	if request.user.is_authenticated():
		return redirect('home')
