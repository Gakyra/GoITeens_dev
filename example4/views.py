from django.shortcuts import render
from .models import Person, Stuff
from .forms import NewUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm


def flush1(request):
    request.session.set_test_cookie()

    test_cookie = request.session.test_cookie_worked()

    if test_cookie:
        pass
    else:
        pass

    old_session_key = request.session.session_key

    request.session["test_value"] = "Hello, session!"
    test_before = request.session.get("test_value", "Not found")

    request.session.flush()  # Очищаємо сесію

    new_session_key = request.session.session_key
    test_after = request.session.get("test_value", "Not found")

    test_cookie_working = request.session.test_cookie_worked()

    context = {
        "stuff": Stuff.objects.all(),
        "stars": range(1, 11),
        "old_session_key": old_session_key,
        "new_session_key": new_session_key,
        "test_before": test_before,
        "test_after": test_after,
        "test_cookie_working": test_cookie_working,
    }

    # request.session.delete_test_cookie()

    return render(request, "flush.html", context)
