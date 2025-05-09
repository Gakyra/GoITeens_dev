from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('flush/', views.flush1, name="flush1"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
