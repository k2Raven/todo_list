from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.views.generic.list import MultipleObjectMixin
from django.contrib.auth.mixins import PermissionRequiredMixin

from webapp.models import Project
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from webapp.forms import ProjectForm, ChangeUsersInProjectForm


class ProjectListView(ListView):
    template_name = 'project/index.html'
    context_object_name = 'projects'

    def get_queryset(self):
        return Project.objects.filter(is_deleted=False).order_by('-date_started')


class ProjectDetail(DetailView, MultipleObjectMixin):
    template_name = 'project/project_view.html'
    paginate_by = 3
    queryset = Project.objects.filter(is_deleted=False)

    def get_context_data(self, **kwargs):
        tasks = self.object.tasks.all()
        context = super().get_context_data(object_list=tasks, **kwargs)
        return context


class ProjectCreate(PermissionRequiredMixin, CreateView):
    model = Project
    template_name = 'project/create.html'
    form_class = ProjectForm
    permission_required = 'webapp.add_project'

    def form_valid(self, form):
        self.object = form.save()
        self.object.users.add(self.request.user)
        return redirect(self.get_success_url())

    def get_success_url(self):
        return reverse('webapp:project_view', kwargs={'pk': self.object.pk})


class ProjectUpdate(PermissionRequiredMixin, UpdateView):
    model = Project
    template_name = 'project/update.html'
    form_class = ProjectForm
    permission_required = 'webapp.change_project'

    def get_success_url(self):
        return reverse('webapp:project_view', kwargs={'pk': self.object.pk})


class ProjectDelete(PermissionRequiredMixin, DeleteView):
    model = Project
    success_url = reverse_lazy('webapp:index')
    permission_required = 'webapp.delete_project'

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.is_deleted = True
        self.object.save()
        return redirect(success_url)


class ChangeUsersInProjectView(PermissionRequiredMixin, UpdateView):
    model = Project
    form_class = ChangeUsersInProjectForm
    template_name = 'project/change_user.html'
    permission_required = 'webapp.add_users_in_project'

    def has_permission(self):
        return super().has_permission() and self.request.user in self.get_object().users.all()

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_success_url(self):
        return reverse('webapp:project_view', kwargs={'pk': self.object.pk})
