from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=100,)
    last_name = models.CharField(max_length=100,)
    email = models.EmailField(unique=True,)
    courses = models.ManyToManyField('Course', related_name='enrolled_students',)

class Course(models.Model):
    name = models.CharField(max_length=200,)
    price = models.DecimalField(max_digits=10, decimal_places=2,)
    description = models.TextField()
    students = models.ManyToManyField(Student, related_name='student_courses',blank=True)
