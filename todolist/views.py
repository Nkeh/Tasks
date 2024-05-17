from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Task


def home(request):
    return render(request, 'todolist/index.html')


def taskList(request):
    tasks = Task.objects.all()

    return render(request, 'todolist/task_list.html', {'tasks': tasks})


def taskDetail(request, pk):
    task = Task.objects.get(pk=pk)
    return render(request, 'todolist/task_detail.html', {'task': task})


def taskCreate(request):
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        deadline = request.POST.get('deadline')

        Task.objects.create(
            title=title,
            description=description,
            deadline=deadline,
        )

        return redirect('/tasks/')

    return render(request, 'todolist/task_create.html')


def taskUpdate(request):
    pass


def taskDelete(request, obj):
    pass