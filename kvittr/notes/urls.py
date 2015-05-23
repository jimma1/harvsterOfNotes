from django.conf.urls import patterns, url, include

from notes.views import index_view, add_note, add_tag, tag_search, detail_note, increase_num_likes


urlpatterns = patterns('',
	url(r'^$', index_view, name='index'),
	url(r'^addnote/', add_note, name='addnote'),
	url(r'^addtag/', add_tag, name='addtag'),
	url(r'^tags/(?P<slug>[-\w]+)/$', tag_search, name='tagsearch'),
	url(r'^detailnote/', detail_note,  name='detailnote'),
	url(r'^\d+/increase_num_likes/$', increase_num_likes, name='increase_numlikes'),
	#url(r'^(\d+)/vote$',vote, name='vote'),
	#url(r'^(\d+)/increase_likes$', likes_note, name="likes_note"),
	#url(r'^(\d+)/add_points/(\d+)$', note_add_likes, name="note_add_likes"),
	)