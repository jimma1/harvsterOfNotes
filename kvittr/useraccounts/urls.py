from django.conf.urls import patterns, url

from useraccounts.views import user_login

urlpatterns = patterns('',
	url(r'^login/',user_login, name='login'),
	)
