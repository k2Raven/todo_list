
from django.urls import path
from webapp.views import IndexView, CreateTask, TaskView, UpdateTask, DeleteTask, ProjectListView, ProjectDetail, \
    ProjectCreate, ProjectDelete, ProjectUpdate, ChangeUsersInProjectView

app_name = 'webapp'

urlpatterns = [
    path('', ProjectListView.as_view(), name='index'),
    path('project/<int:pk>/', ProjectDetail.as_view(), name='project_view'),
    path('project/<int:pk>/delete/', ProjectDelete.as_view(), name='project_delete'),
    path('project/<int:pk>/update/', ProjectUpdate.as_view(), name='project_update'),
    path('project/<int:pk>/change-users/', ChangeUsersInProjectView.as_view(), name='change_users'),
    path('project/add/', ProjectCreate.as_view(), name='project_add'),
    path('task/', IndexView.as_view(), name='tasks_list'),
    path('task/<int:pk>/add/', CreateTask.as_view(), name='task_add'),
    path('task/<int:pk>/', TaskView.as_view(), name='task_view'),
    path('task/<int:pk>/update/', UpdateTask.as_view(), name='task_update'),
    path('task/<int:pk>/delete/', DeleteTask.as_view(), name='task_delete'),
]