from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import CreateTask, EditTask
from .models import Task
from django.views.generic import ListView, CreateView, UpdateView 

# Display list of tasks.

class TaskListView(ListView):
	queryset = Task.objects.all()
	template_name = 'todo/todo_list.html'


# Display form for creating task

class TaskCreateView(CreateView, TaskListView):
	form_class = CreateTask

	def get_success_url(self):
		return reverse('todo:TaskListView')


# Delete task

def delete_task(request, task_id):
	the_task = Task.objects.get(pk=task_id)
	the_task.delete()
	return redirect('todo:TaskListView')

# Marks task as complete

def actioned_task(request, task_id):
	the_task = Task.objects.get(pk=task_id)
	the_task.actioned = True
	the_task.save()
	return redirect('todo:TaskListView')


# Dsiplay view to edit tasks

def edit_task(request, id):
	the_task = Task.objects.get(pk=id)
	form = EditTask(instance=the_task)
	if request.method == 'POST':
		form = EditTask(request.POST, instance=the_task)
		if form.is_valid():
			form.save()
			return redirect('todo:TaskListView')
	return render(request, 'todo/edit_vi_tamplate.html', {'form' : form})


