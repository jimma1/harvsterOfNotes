from django.db import models
from django.contrib.auth.models import User

from useraccounts.models import Member
'''
Searching in tags with GET request to a special crafted url.
Must use slugify in Django, which only accept letters, numbers, underscores and hyphens
'''

# Create your models here.
class Note(models.Model):
	label = models.CharField(max_length = 15)
	body = models.TextField(max_length=333)
	# populate field with time of note creation
	timestamp = models.DateTimeField(auto_now_add=True)
	# a note may have zero or many tags
	tags = models.ManyToManyField('Tag', related_name='notes')
	author = models.ForeignKey(User)
	num_likes = models.PositiveIntegerField(default=0)

	def __unicode__(self):
		return self.label

class Tag(models.Model):
	label = models.CharField(max_length = 20)
	slug = models.SlugField(max_length=20)

	def __unicode__(self):
		return self.label
