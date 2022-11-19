from django.shortcuts import render, get_object_or_404, redirect
from webapp.models import Task, STATUS_CHOICES


def index_view(request):
    if request.method == "POST":
        task_id = request.GET.get('id')
        task = Task.objects.get(id=task_id)
        task.delete()
        return redirect('index')

    tasks = Task.objects.all()
    return render(request, 'index.html', {'tacks': tasks})


def task_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'task_view.html', {'task': task})


def create_task(request):
    if request.method == "GET":
        return render(request, 'create.html', {'statuses': STATUS_CHOICES})
    elif request.method == "POST":
        title = request.POST.get('title')
        status = request.POST.get('status')
        deadline = request.POST.get('deadline')
        description = request.POST.get('description')
        if not deadline:
            deadline = None
        new_task = Task.objects.create(title=title, status=status, deadline=deadline, description=description)
        return redirect('task_view', pk=new_task.pk)
