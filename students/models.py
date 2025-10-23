from django.db import models

# Create your models here.

class Students (models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField() 
    grade=models.CharField(max_length=10)
    city=models.CharField(max_length=100)

    def __str__(self):
        return self.name
        