from urllib import request
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from django.contrib import messages
from django.views.generic import TemplateView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from .models import Task
from .forms import TaskForm


class IndexView(TemplateView):
    template_name = "todolist/index.html"


class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = "tasks"
    login_url = '/admin'

    def get_queryset(self):
        return self.request.user.tasks.filter(completed=False)
    


@login_required(login_url='login')
def taskDetail(request, task_id):
   task = get_object_or_404(Task, pk=task_id)
   return render(request, 'todolist/task_detail.html', {'task': task})


@login_required(login_url='login')
def create_task(request):
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        deadline = request.POST.get('deadline')
        user = request.user

        task = Task(
            title = title,
            description = description,
            deadline = deadline,
            user = user
        )
        task.save()

        return redirect('task.list')

    return render(request, 'todolist/task_create.html')


@login_required(login_url='login')
def update_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if request.method == "POST":

        form = TaskForm(request.POST, instance=task)

        if form.is_valid():
            form.save()
            return redirect('task.detail', task_id=task_id)
        else:
            messages.error(request, "Invalid Field(s)")

    else:
        form = TaskForm(instance=task)

    return render(request, 'todolist/task_update.html', {'form': form})


@login_required(login_url='login')
def taskDelete(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        task.delete()
        return redirect('task.list')  # Redirect to the task list after deletion
    return render(request, 'todolist/task_confirm_delete.html', {'task': task})