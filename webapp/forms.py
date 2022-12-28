from django import forms
from django.contrib.auth import get_user_model
from django.forms import widgets
from webapp.models import Type, Status, Task, Project


# class TaskForm(forms.Form):
#     title = forms.CharField(max_length=60, required=True, label='Название')
#     description = forms.CharField(max_length=3000, required=False, label='Описание', widget=widgets.Textarea)
#     status = forms.ModelChoiceField(queryset=Status.objects.all(), required=True, label='Статус')
#     types = forms.ModelMultipleChoiceField(queryset=Type.objects.all(), label='Тип')

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        exclude = ['project']


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'date_started', 'date_end']

class ChangeUsersInProjectForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super().__init__(*args, **kwargs)
        self.fields['users'].queryset = get_user_model().objects.exclude(pk=self.user.pk)
    class Meta:
        model = Project
        fields = ['users']
        widgets = {'users' : widgets.CheckboxSelectMultiple}

    def save(self, commit=True):
        project = super().save(commit=commit)

        if commit:
            project.users.add(self.user)
            project.save()

        return project


class SearchForm(forms.Form):
    search = forms.CharField(max_length=60, required=False, label='')
