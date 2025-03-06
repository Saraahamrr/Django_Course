from django.db import models

# Create your models here.
class Classroom(models.Model):
    name = models.CharField(max_length=30)
    subject = models.ForeignKey('Subject', on_delete=models.CASCADE,related_name='classrooms')
    year = models.IntegerField()
    teacher = models.CharField(max_length=30)
    student = models.ForeignKey('Student', on_delete=models.CASCADE,related_name='classrooms')
    School = models.ForeignKey('School', on_delete=models.CASCADE,related_name='classrooms_associated' ,default=1, null=True, blank=True)
    area = models.FloatField(null=True, blank=True)
    
    def save (self,*args,**kwargs):
        if self.area == None:
            self.area = 0
        else:
            self.area = round(self.area,2)
            super(Classroom,self).save(*args,**kwargs)
    def __str__(self):
        return self.name


    
    
class Subject(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    def __str__(self):
        return self.name
    
class School(models.Model):
    name = models.CharField(max_length=30)
    address = models.TextField()
    classrooms = models.ForeignKey(Classroom, on_delete=models.CASCADE, related_name='schools')
    area = models.FloatField()
    def save (self,*args,**kwargs):
        if self.area == None:
            self.area = 0
        else:
            self.area = round(self.area,2)
            super(School,self).save(*args,**kwargs)
    
    def __str__(self):
        return self.name
    
class Student(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    def __str__(self):
        return self.name
    
class Teacher(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name