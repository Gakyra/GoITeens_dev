from django.shortcuts import render, get_object_or_404
from .models import Student, Course

def student_courses(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    courses = student.courses.all()
    return render(request, 'student_courses.html', {'student': student, 'courses': courses})

def course_students(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    students = course.students.all()
    return render(request, 'course_students.html', {'course': course, 'students': students})
