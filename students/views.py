from django.shortcuts import render,redirect

from rest_framework import viewsets
from .models import Students
from .serializers import StudentSerializer
from .forms import StudentForm


# Create your views here.
class StudentViewSet(viewsets.ModelViewSet):
    queryset=Students.objects.all()
    serializer_class=StudentSerializer



def add_student(request):
    if request.method=='POST':
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list') 
    else:
        form=StudentForm()
    return render(request,'students/student_form.html',{'form':form})
            


def student_list(request):
    students=Students.objects.all()
    return render(request,'students/student_list.html',{'students':students})