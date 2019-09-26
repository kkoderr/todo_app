""" test_detail_view_link
	test_edit
	test_delete"""

from django.test import TestCase


from .models import Task
from django.urls import reverse


class AppTests(TestCase):
	def setUp(self):
		task = Task.objects.create(
			task='New test task',
			category='none', 
			actioned=False
		)


	def test_update_post(self):
		update = Task.objects.first()
		update.task ='this is update'
		update.save()
		tasks = Task.objects.count()

		self.assertEqual(tasks, 1)


	def test_detail_view_link(self):
		pass