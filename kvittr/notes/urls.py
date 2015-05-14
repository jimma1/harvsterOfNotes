from django.conf.urls import patterns, url, include

from notes.views import index_view, add_note


urlpatterns = patterns('',
	url(r'^$', index_view, name='index'),
	url(r'^addnote/', add_note, name='addnote'),
	)