from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'myClassroom/index.html', {})

def about(request): 
    return render(request, 'myClassroom/about.html', {})
