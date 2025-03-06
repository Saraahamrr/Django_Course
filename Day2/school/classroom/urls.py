from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('classroom', views.Formclassroom, name='formClassroom'),
    path('school', views.FormSchool, name='formSchool'),
    ]