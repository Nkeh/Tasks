from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from django.views.generic import TemplateView, ListView, DetailView

from .models import Task
from .forms import TaskForm


class IndexView(TemplateView):
    template_name = "todolist/index.html"


class TaskListView(ListView):
    model = Task
    context_object_name = "tasks"

    def get_queryset(self):
        return Task.objects.all()[:10]
    

def taskDetail(request, task_id):
   task = get_object_or_404(Task, pk=task_id)
   return render(request, 'todolist/task_detail.html', {'task': task})


def create_task(request):
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        deadline = request.POST.get('deadline')

        task = Task(
            title = title,
            description = description,
            deadline = deadline
        )
        task.save()

        return redirect('/tasks/')

    return render(request, 'todolist/task_create.html')


def update_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if request.method == "POST":

        form = TaskForm(request.POST, instance=task)

        if form.is_valid():
            form.save()

            return redirect('/tasks/')

    else:
        form = TaskForm(instance=task)

    return render(request, 'todolist/task_update.html', {'form': form})


def taskDelete(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        task.delete()
        return redirect('/tasks/')  # Redirect to the task list after deletion
    return render(request, 'todolist/task_confirm_delete.html', {'task': task})