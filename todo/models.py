from django.db import models
from django.urls import reverse

#  Model for different task fields.

CATEGORY = (
	('None', 'none'),
	('Work','work'), 
	('Personal', 'personal'), 
	('Study','study'), 
	('Research','research')
	)

class Task(models.Model):
	task = models.CharField(max_length=100, verbose_name= 'New Task')
	date_created = models.DateTimeField(auto_now_add=True)
	category = models.CharField(max_length=100, choices=CATEGORY, default='none', verbose_name='Choose Category')
	actioned = models.BooleanField(default=False)

	def __str__(self):
		return self.task

	def get_absolute_url(self):
		return reverse('todo:TaskListView', kwargs={"id": self.id})
		#return reverse('todo:TaskListView')
