from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib import messages

from useraccounts.forms import LoginForm, RegistrationForm, UserupdateForm

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
			messages.add_message(request, messages.INFO, 'User successfully registered. Login to add notes')
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

def user_update(request):
	context = {}
	if request.method == 'POST':
		# instance is logged in user
		form = UserupdateForm(request.POST, instance=request.user)
		if form.is_valid():
			form.save()
			context['update_ok'] = True
			return render(request, 'useraccounts/update.html', context)
	# not post
	else:
		# fill in existing userinfo in form
		initial_args = {
			"first_name":request.user.first_name,
			"last_name":request.user.last_name,
			"email":request.user.email
		}
		form = UserupdateForm(initial=initial_args)

	context['form'] = form
	return render (request, 'useraccounts/update.html', context)
