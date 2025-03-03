from django.contrib import admin
from .models import Classroom
from .models import Subject
from .models import School
from .models import Student




# Register your models here.
admin.site.register(Classroom)
admin.site.register(Subject)
admin.site.register(School)
admin.site.register(Student)

