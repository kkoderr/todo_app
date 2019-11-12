from django.db import models
from django.urls import reverse


class Task(models.Model):
	"""The Task table fields """

	task = models.CharField(max_length=100, verbose_name= 'New Task')
	date_created = models.DateTimeField(auto_now_add=True)
	none = models.BooleanField(default=False)
	work = models.BooleanField(default=False)
	personal = models.BooleanField(default=False)
	study = models.BooleanField(default=False)
	research = models.BooleanField(default=False)
	actioned = models.BooleanField(default=False)

	def __str__(self):
		return self.task
