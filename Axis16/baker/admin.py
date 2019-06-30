from django.contrib import admin
from .models import Baker_Questions


class Baker_Que_Admin(admin.ModelAdmin):
    list_display = ['name', 'answer', 'level']
    ordering = ['level']
    class Meta:
        model = Baker_Questions

admin.site.register(Baker_Questions, Baker_Que_Admin)
