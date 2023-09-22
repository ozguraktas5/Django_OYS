from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_student, name='register_student'),
    path('enroll/', views.enroll_course, name='enroll_course'),
]
