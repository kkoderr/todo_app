from django.contrib import admin
from django.urls import path
from . import views

# Url routes of the different views

app_name = 'todo'
urlpatterns = [ 
			path('', views.TaskCreateView.as_view(), name='TaskCreateView'),
			path('', views.TaskListView.as_view(), name='TaskListView'),
			path('<task_id>/actioned', views.actioned_task, name='actioned_task'),
			path('<task_id>/delete', views.delete_task, name='delete_task'),
			path('<int:id>/lala/', views.edit_task, name='edit_task')
	]