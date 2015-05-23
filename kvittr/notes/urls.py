from django.conf.urls import patterns, url, include

from notes.views import index_view, add_note, add_tag, tag_search, detail_note


urlpatterns = patterns('',
	url(r'^$', index_view, name='index'),
	url(r'^addnote/', add_note, name='addnote'),
	url(r'^addtag/', add_tag, name='addtag'),
	url(r'^tags/(?P<slug>[-\w]+)/$', tag_search, name='tagsearch'),
	url(r'^detailnote/', detail_note,  name='detailnote'),
	)