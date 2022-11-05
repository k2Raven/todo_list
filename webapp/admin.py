from django.contrib import admin
from webapp.models import Task


class TackAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'status', 'deadline']
    list_filter = ['status']
    search_fields = ['title']
    exclude = []


admin.site.register(Task, TackAdmin)