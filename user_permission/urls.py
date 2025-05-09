from django.urls import path
from . import views

urlpatterns = [
        path('user_auth_view/', views.user_auth_view, name='user_auth_view'),
]
