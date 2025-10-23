from django.urls import path,include
from .views import  StudentViewSet,student_list,add_student
from rest_framework import routers

router=routers.DefaultRouter()
router.register(r'students',StudentViewSet)

urlpatterns=[
    path('',student_list,name='student_list'),
    path('add/',add_student,name='add_student'),

    
    path('api/',include(router.urls)),

]