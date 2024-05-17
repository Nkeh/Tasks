from django.urls import path

from . import views

urlpatterns = [
    path('', views.home),
    path('tasks/', views.taskList, name="task.list"),
    path('tasks/<int:pk>/', views.taskDetail, name="task.detail"),
    path("tasks/create/", views.taskCreate, name="task.new")
]
