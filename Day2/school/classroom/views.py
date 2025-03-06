from django.shortcuts import render
from .models import Classroom
from .models import Subject
from .models import School
from .models import Student
from .models import Teacher

# Create your views here.
def home(request):
    return render(request, 'myClassroom/index.html', {
        'classrooms': Classroom.objects.all(),
        'subjects': Subject.objects.all(),
        'schools': School.objects.all(),
        'students': Student.objects.all
    })

def Formclassroom(request): 
    students = Student.objects.all()
    subjects = Subject.objects.all()
    schools = School.objects.all()
    teachers = Teacher.objects.all()
    

    
    if request.method == 'POST':
            
        # student_name = None
        # subject_name = None
        # school_name = None
        
        name = request.POST.get('name')
        subject_name = request.POST.get('subject')
        year = request.POST.get('year')
        teacher_name = request.POST.get('teacher')
        student_name = request.POST.get('student')
        school_name = request.POST.get('School')
        area = request.POST.get('area')
        
        
    
        student_instance = Student.objects.get(name=student_name)
        subject_instance = Subject.objects.get(name=subject_name)
        school_instance = School.objects.get(name=school_name)
        teacher_instance = Teacher.objects.get(name = teacher_name)
        area = float(area)
     
        data = Classroom(name=name,
                     subject=subject_instance, 
                     year=year,
                     teacher=teacher_instance,
                     student=student_instance, 
                     School=school_instance,
                     area=area
                    )                                                               
        data.save()
    
    return render(request, 'myClassroom/FormClassroom.html', {'students': students, 'subjects': subjects, 'schools': schools, 'teachers' : teachers})

def FormSchool(request): 
    
    Classrooms = Classroom.objects.all()    
    if request.method == 'POST':

        name = request.POST.get('name')
        address = request.POST.get('address')
        area = request.POST.get('area')    
        Classrooms_name = request.POST.get('classrooom')
        
        classroom_instance = Classroom.objects.get(name=Classrooms_name)
        area = float(area)
        
        
        data = School (
            name = name,
            address = address,
            area = area,
            classrooms=classroom_instance
        )
        data.save()
        
    return render(request, 'myClassroom/FormSchool.html', {'classrooms':Classrooms})
