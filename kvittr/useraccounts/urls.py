from django.conf.urls import patterns, url

from useraccounts.views import user_login, user_logut, user_registration

urlpatterns = patterns('',
	url(r'^login/',user_login, name='login'),
	url(r'^logout$', user_logut, name='logout'),
	url(r'^register$', user_registration, name='register'),
	)
