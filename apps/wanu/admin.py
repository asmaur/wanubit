from django.contrib import admin

# Register your models here.
from .models import *

class ProjectAdmin(admin.ModelAdmin):

    list_display = ('name', 'url', 'created')


admin.site.register(Project, ProjectAdmin)
