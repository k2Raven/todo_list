from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.contrib.auth.mixins import PermissionRequiredMixin

from webapp.models import Task, Project
from webapp.forms import TaskForm, SearchForm
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
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


class CreateTask(PermissionRequiredMixin, CreateView):
    template_name = 'task/create.html'
    model = Task
    form_class = TaskForm
    permission_required = 'webapp.add_task'

    def has_permission(self):
        project = get_object_or_404(Project, pk=self.kwargs['pk'])
        return super().has_permission() and self.request.user in project.users.all()

    def form_valid(self, form):
        form.instance.project = get_object_or_404(Project, pk=self.kwargs.get('pk'))
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('webapp:project_view', kwargs={'pk': self.object.project.pk})


class UpdateTask(PermissionRequiredMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'task/update.html'
    permission_required = 'webapp.change_task'

    def has_permission(self):
        return super().has_permission() and self.request.user in self.get_object().project.users.all()

    def get_success_url(self):
        return reverse('webapp:project_view', kwargs={'pk': self.object.project.pk})


class DeleteTask(PermissionRequiredMixin, DeleteView):
    model = Task
    template_name = 'task/delete.html'
    permission_required = 'webapp.delete_task'

    def has_permission(self):
        return super().has_permission() and self.request.user in self.get_object().project.users.all()

    def get_success_url(self):
        return reverse('webapp:project_view', kwargs={'pk': self.object.project.pk})
