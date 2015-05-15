from django.conf.urls import patterns, url, include

from notes.views import index_view, add_note, add_tag


urlpatterns = patterns('',
	url(r'^$', index_view, name='index'),
	url(r'^addnote/', add_note, name='addnote'),
	url(r'^addtag/', add_tag, name='addtag'),
	)