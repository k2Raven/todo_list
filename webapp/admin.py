from django.contrib import admin
from webapp.models import Task, Status, Type


class TackAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'status']
    list_filter = ['status']
    search_fields = ['title']
    exclude = []


admin.site.register(Task, TackAdmin)
admin.site.register(Status)
admin.site.register(Type)
