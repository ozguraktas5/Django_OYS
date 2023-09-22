from django import forms
from .models import Student, Course

class StudentRegistrationForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'birth_date']
        
class CourseEnrollmentForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['course_name']