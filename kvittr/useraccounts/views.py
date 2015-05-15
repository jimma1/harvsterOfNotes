from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from useraccounts.forms import LoginForm

# Create your views here.
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
