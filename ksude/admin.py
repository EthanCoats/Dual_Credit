from django.contrib import admin
from .models import Teacher
from .models import School


# Register your models here.
admin.site.register(School)
admin.site.register(Teacher)