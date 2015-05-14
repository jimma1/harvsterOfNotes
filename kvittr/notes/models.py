from django.db import models

# Create your models here.
class Note(models.Model):
	label = models.CharField(max_length = 30)
	body = models.TextField()
	# populate field with time of note creation
	timestamp = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.label
