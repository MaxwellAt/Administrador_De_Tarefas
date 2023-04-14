from django.urls import path
from . import views


urlpatterns = [
    path('', views.task_list, name='taskList'),
    path('tasks/', views.task_create, name='tasksAdmin'),
]