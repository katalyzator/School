from django.contrib import admin

# Register your models here.
from main.models import *


class TeacherAdmin(admin.ModelAdmin):
    class Meta:
        model = Teachers


admin.site.register(Teachers, TeacherAdmin)

admin.site.register(Publication)
