from django import forms 
from .models import Students 

class StudentForm(forms.ModelForm):
    class Meta:
        model=Students
        fields=['name','age','grade','city']