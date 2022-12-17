from django.core.paginator import Paginator
from django.urls import reverse
from django.views.generic.list import MultipleObjectMixin

from webapp.models import Project
from django.views.generic import ListView, DetailView, CreateView
from webapp.forms import ProjectForm

class ProjectListView(ListView):
    template_name = 'project/index.html'
    model = Project
    context_object_name = 'projects'
    ordering = '-date_started'

class ProjectDetail(DetailView, MultipleObjectMixin):
    model = Project
    template_name = 'project/project_view.html'
    paginate_by = 3

    def get_context_data(self, **kwargs):
        tasks = self.object.tasks.all()
        context = super().get_context_data(object_list=tasks, **kwargs)
        return context

class ProjectCreate(CreateView):
    model = Project
    template_name = 'project/create.html'
    form_class = ProjectForm

    def get_success_url(self):
        return reverse('project_view', kwargs={'pk': self.object.pk})
