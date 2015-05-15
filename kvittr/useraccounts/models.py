from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Member(models.Model):
	user = models.OneToOneField(User)
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)

	def __unicode__(self):
		return self.first_name
