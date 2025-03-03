from django.shortcuts import render
from .models import Classroom
from .models import Subject
from .models import School
from .models import Student

# Create your views here.
def home(request):
    return render(request, 'myClassroom/index.html', {
        'classrooms': Classroom.objects.all(),
        'subjects': Subject.objects.all(),
        'schools': School.objects.all(),
        'students': Student.objects.all
    })

def about(request): 
    return render(request, 'myClassroom/about.html', {})
