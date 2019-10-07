
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


	def test_create_link(self):
		data = {
			'task': 'My new task', 
			'category':'personal', 
			'actioned':False}

		url = reverse("todo:TaskCreateListView") 
		response = self.client.post(url, data)

		self.assertEqual(response.status_code, 200)
		self.assertContains(response, data['task'])


	def test_editview_link(self):
		url = reverse("todo:edit_task", kwargs={"id":self.task.id})
		response = self.client.get(url)

		self.assertEqual(response.status_code, 200) 

	def test_editview_redirects_on_complete(self):
		data = {'task':'This is update'}
		instance=self.task.id
		url = reverse("todo:edit_task", kwargs={"id":self.task.id})
		response = self.client.post(url, data)

		self.assertEqual(response.status_code, 302)


	def test_update_post(self):
		update = Task.objects.first()
		update.task ='this is update'
		update.save()

		self.assertEqual(self.task, update)


