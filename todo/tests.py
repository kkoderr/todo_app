""" test_detail_view_link
	test_edit
	test_delete"""

from django.test import TestCase


from .models import Task
from django.urls import reverse


class AppTests(TestCase):
	def setUp(self):
		self.task = Task.objects.create(
			task='New test task',
			category='none', 
			actioned=False
		)


	def test_update_post(self):
		update = Task.objects.first()
		update.task ='this is update'
		update.save()

		self.assertEqual(self.task, update)


	def test_edit_view_link(self):
		url = reverse("todo:edit_task", kwargs={"id":self.task.id})
		response = self.client.get(url)
		self.assertEqual(response.status_code, 200)