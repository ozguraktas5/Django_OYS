from django.db import models

class Teacher(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    expertise = models.CharField(max_length=100, default="")
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Course(models.Model):
    course_name = models.CharField(max_length=100)
    course_code = models.CharField(max_length=20, unique=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, blank=True)
    schedule = models.TextField()
    
    def __str__(self):
        return self.course_name
    
class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField()
    registration_date = models.DateField(auto_now_add=True)
    class_teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
