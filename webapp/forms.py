from django import forms
from django.forms import widgets
from webapp.models import Type, Status


class TaskForm(forms.Form):
    title = forms.CharField(max_length=60, required=True, label='Название')
    description = forms.CharField(max_length=3000, required=False, label='Описание', widget=widgets.Textarea)
    status = forms.ModelChoiceField(queryset=Status.objects.all(), required=True, label='Статус')
    type = forms.ModelChoiceField(queryset=Type.objects.all(), required=True, label='Тип')

