from django import forms
from .models import Task

# Creates a form for CreateView

class CreateTask(forms.ModelForm):
	class Meta:
		model = Task
		fields = [
			'task','work','personal','study','research','none'
		]

class EditTask(forms.ModelForm):
	class Meta:
		model = Task
		fields = ['task']
