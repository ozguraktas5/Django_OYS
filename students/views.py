from django.shortcuts import render, redirect
from .forms import StudentRegistrationForm, CourseEnrollmentForm

def register_student(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_page')
    else:
        form = StudentRegistrationForm()
    return render(request, 'students/register_student.html', {'form': form})

def enroll_course(request):
    if request.method == 'POST':
        form = CourseEnrollmentForm(request.POST)
        if form.is_valid():
            return redirect('success_page') 
    else:
        form = CourseEnrollmentForm()
    return render(request, 'students/enroll_course.html', {'form': form})


