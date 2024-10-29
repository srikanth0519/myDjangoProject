from django.shortcuts import HttpResponse, render
from .models import Student


# Create your view here
def home(request):
    return HttpResponse("Welcome to Django Training Class")

def index(request):
    our_dict = {'Srikanth':"This is Django project and we are writing this in myDjangoProject_app1/index.html!"}
    return render(request,'myDjangoProject_app1/index.html', context=our_dict)

def student_table(request):
    students = Student.objects.all()
    return render(request, 'myDjangoProject_app1/student_table.html', {'students':students})