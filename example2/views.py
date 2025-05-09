import datetime
from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib.auth.forms import PasswordResetForm
from django.template.loader import render_to_string


def login_view(request):
    username = "not logged in"

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            response = render(request, 'loggedin.html', {"username": username})

            response.set_cookie('last_connection', datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            response.set_cookie('username', username)
            return response
    else:
        form = LoginForm()

    return render(request, 'login.html', {"form": form})


def form_view(request):
    if 'username' in request.COOKIES and 'last_connection' in request.COOKIES:
        username = request.COOKIES['username']
        last_connection = request.COOKIES['last_connection']

        try:
            last_connection_time = datetime.datetime.strptime(last_connection, "%Y-%m-%d %H:%M:%S")
            if (datetime.datetime.now() - last_connection_time).seconds < 10:
                return render(request, 'loggedin.html', {"username": username})
        except ValueError:
            pass

    return render(request, 'login.html', {"form": LoginForm()})


def password_reset_request(request):
    if request.method == "POST":
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            associated_users = User.objects.filter(Q(email=data))
            if associated_users.exists():
                for user in associated_users:
                    subject = "Password Reset Requested"
                    email_template_name = "main/password/password_reset_email.txt"
                    c = {
                        "email": user.email,
                        'domain': '127.0.0.1:8000',
                        'site_name': 'Website',
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        "user": user,
                        'token': default_token_generator.make_token(user),
                        'protocol': 'http',
                    }
                    email = render_to_string(email_template_name, c)
                    try:
                        send_mail(subject, email, 'admin@example.com', [user.email], fail_silently=False)
                    except BadHeaderError:
                        return HttpResponse('Invalid header found.')
                    return redirect("/password_reset/done/")
    password_reset_form = PasswordResetForm()
    return render(request=request, template_name="main/password/password_reset.html",
                  context={"password_reset_form": password_reset_form})



def password_reset(request):
    return render(request, 'password_reset.html')


def password_reset_done(request):
    return render(request, 'password_reset_done.html')


def password_reset_confirm(request):
    return render(request, 'password_reset_confirm.html')


def password_reset_complete(request):
    return render(request, 'password_reset_complete.html')






