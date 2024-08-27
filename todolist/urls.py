from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name="home"),
    path('tasks/', views.TaskListView.as_view(), name="task.list"),
    path('tasks/<int:task_id>/', views.taskDetail, name="task.detail"),
    path('tasks/<int:task_id>/update/', views.update_task, name="task.update"),
    path('tasks/<int:task_id>/delete/', views.taskDelete, name='task.delete'),
    path("tasks/create/", views.create_task, name="task.new")
]
