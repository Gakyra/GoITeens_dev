from django.urls import path
from . import views

urlpatterns = [
    path('student/<int:student_id>/', views.student_courses, name='student_courses'),
    path('course/<int:course_id>/', views.course_students, name='course_students'),
]
