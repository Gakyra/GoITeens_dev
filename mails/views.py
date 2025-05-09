from django.core.mail import BadHeaderError, EmailMessage
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from .forms import EmailForm
from django.http import HttpResponse
from .logger import log_message


def is_valid_email(email):
    """Проверка корректности email."""
    try:
        validate_email(email)
        return True
    except ValidationError:
        return False

def send_email_view(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            # Fetching data from form
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            recipient = form.cleaned_data['recipient']

            if not is_valid_email(recipient):
                return HttpResponse("Invalid recipient email address.")

            try:
                # Send email
                email = EmailMessage(
                    subject,
                    message,
                    'maks3010dan@gmail.com',
                    ['belosokhovmaks@gmail.com']
                )
                email.send()
            except BadHeaderError:
                return HttpResponse("Invalid header found.")
            except Exception as e:
                return HttpResponse(f"Error while sending email: {e}")


            return render(request, 'send_email.html', {'form': form, 'success': True})
    else:

        form = EmailForm()

    return render(request, 'send_email.html', {'form': form})



def my_view(request):
    log_message("This is a test log")
    return HttpResponse("Log is triggered!")