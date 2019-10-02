from django.contrib import admin
from django.urls import path
from . import views

# Url routes of the different views

app_name = 'todo'
urlpatterns = [ 
			path('', views.TaskCreateListView, name='TaskCreateListView'),
			path('<task_id>/actioned', views.actioned_task, name='actioned_task'),
			path('<task_id>/delete', views.delete_task, name='delete_task'),
			path('<int:id>/edit/', views.edit_task, name='edit_task'),
			path('<task_id>/undo_actioned', views.undo_actioned_task, name='undo_actioned_task'),
	]