from django.db import models

# Create your models here.
class Classroom(models.Model):
    name = models.CharField(max_length=30)
    subject = models.ForeignKey('Subject', on_delete=models.CASCADE,related_name='classrooms')
    year = models.IntegerField()
    teacher = models.CharField(max_length=30)
    student = models.ForeignKey('Student', on_delete=models.CASCADE,related_name='classrooms')
    def __str__(self):
        return self.name


    
    
class Subject(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    def __str__(self):
        return self.name
    
class School(models.Model):
    name = models.CharField(max_length=30)
    number_of_classrooms = models.IntegerField(models.Count('classrooms'))
    address = models.TextField()
    classrooms = models.OneToOneField(Classroom,on_delete=models.CASCADE,related_name='schools')
    
    
    def __str__(self):
        return self.name
    
class Student(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    def __str__(self):
        return self.name