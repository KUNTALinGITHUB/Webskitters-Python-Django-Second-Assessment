from django.shortcuts import render, redirect
from .models import Student

# This view handles adding student data (all POST requests) and showing the form (all GET requests)
def add_student(request):
    # If form is submitted
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        course = request.POST.get('course')
        marks = request.POST.get('marks')

        # insert data to database
        Student.objects.create(
            name=name,
            email=email,
            course=course,
            marks=marks
        )

        # Redirect after successful submission
        return redirect('view_students')

    # If GET request → show empty form
    return render(request, 'add_student.html')


# This view retrieves and displays all students
def view_students(request):
    students = Student.objects.all()

    return render(request, 'view_students.html', {'students': students})