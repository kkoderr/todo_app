from django import forms
from .models import Task

# Creates a form for CreateView

class CreateTask(forms.ModelForm):
	class Meta:
		model = Task
		fields = [
			'task',
			'category'
		]


	