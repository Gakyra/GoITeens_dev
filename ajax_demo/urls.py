from django.urls import path
from . import views

urlpatterns = [
    path('', views.clock_view, name='clock'),
    path('get-time/', views.get_time, name='get_time'),
]
