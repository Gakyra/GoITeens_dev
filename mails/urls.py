from django.http import HttpResponse
from django.urls import path
from .views import send_email_view

urlpatterns = [
    # path("contact/", send_email, name="contact"),
    path("contact/thanks/", lambda request: HttpResponse("Thank you for your message!"), name="thanks"),
    path('send-email/', send_email_view, name='send_email'),
]
