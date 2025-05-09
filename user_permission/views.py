from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


def user_auth_view(request):
    if request.method == 'POST' and 'register' in request.POST:
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        last_name = request.POST['last_name']

        user = User.objects.create_user(username=username, email=email, password=password)
        user.last_name = last_name
        user.save()

        return HttpResponse("User created successfully! Please log in.")

    elif request.method == 'POST' and 'login' in request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse("Invalid login credentials.")

    elif request.method == 'POST' and 'logout' in request.POST:
        logout(request)
        return redirect('home')

    return render(request, 'auth_page.html')
