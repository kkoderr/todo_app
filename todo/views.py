from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import CreateTask, EditTask
from .models import Task
from django.views.generic import ListView, CreateView, UpdateView



def TaskCreateListView(request):
	# Display list of tasks.
	form = CreateTask()
	if request.method == 'POST':
		form = CreateTask(request.POST)
		if form.is_valid():
			form.save()
			form = CreateTask()

	object_list = Task.objects.all()
	context = {
				'object_list': object_list,
				'form': form
		}

	return render(request, 'todo/todo_list.html', context)


def delete_task(request, task_id):
	the_task = Task.objects.get(pk=task_id)
	the_task.delete()
	return redirect('todo:TaskCreateListView')


# Marks task as complete

def actioned_task(request, task_id):
	the_task = Task.objects.get(pk=task_id)
	the_task.actioned = True
	the_task.save()
	return redirect('todo:TaskCreateListView')


# Undos complete

def undo_actioned_task(request, task_id):
	the_task = Task.objects.get(pk=task_id)
	the_task.actioned = False
	the_task.save()
	return redirect('todo:TaskCreateListView')


# Dsiplay view to edit tasks

def edit_task(request, id):
	the_task = Task.objects.get(pk=id)
	form = EditTask(instance=the_task)
	if request.method == 'POST':
		form = EditTask(request.POST, instance=the_task)
		if form.is_valid():
			form.save()
			return redirect('todo:TaskCreateListView')
	return render(request, 'todo/edit_vi_tamplate.html', {'form' : form})
