from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from webapp.models import Task, Project
from webapp.forms import TaskForm, SearchForm
from django.views.generic import TemplateView, View, DetailView, CreateView
from webapp.views import SearchView


class IndexView(SearchView):
    template_name = 'task/index.html'
    model = Task
    context_object_name = 'tasks'
    paginate_by = 2
    search_form_class = SearchForm
    queryset = Task.objects.filter(project__is_deleted=False)
    search_fields = ['title__icontains', 'description__icontains']

    def post(self, request, *args, **kwargs):
        for task_pk in request.POST.getlist('tasks', []):
            self.model.objects.get(pk=task_pk).delete()
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)


class TaskView(DetailView):
    template_name = 'task/task_view.html'
    model = Task
    queryset = Task.objects.filter(project__is_deleted=False)


class CreateTask(CreateView):
    template_name = 'task/create.html'
    model = Task
    form_class = TaskForm

    def form_valid(self, form):
        form.instance.project = get_object_or_404(Project, pk=self.kwargs.get('pk'))
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('project_view', kwargs={'pk': self.object.project.pk})


class UpdateTask(View):
    def get(self, request, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs['pk'])
        if task.project.is_deleted:
             raise Http404
        form = TaskForm(instance=task)
        return render(request, 'task/update.html', {'form': form, 'task': task})

    def post(self, request, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs['pk'])

        if task.project.is_deleted:
             raise Http404
        form = TaskForm(instance=task, data=request.POST)
        if form.is_valid():
            # task.title = form.cleaned_data['title']
            # task.description = form.cleaned_data['description']
            # task.status = form.cleaned_data['status']
            # task.save()
            # task.types.set(form.cleaned_data['types'])
            task = form.save()
            return redirect('task_view', pk=task.pk)
        else:
            return render(request, 'task/update.html', {'form': form, 'task': task})


class DeleteTask(View):
    def get(self, request, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs['pk'])

        if task.project.is_deleted:
             raise Http404
        return render(request, 'task/delete.html', {'task': task})

    def post(self, request, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs['pk'])
        if task.project.is_deleted:
             raise Http404
        task.delete()
        return redirect('index')
