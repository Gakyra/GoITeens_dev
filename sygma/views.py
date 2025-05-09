from django.shortcuts import render, redirect
from .forms import StuffForm
from .models import Stuff
from .signals import stuff_added_signal


def add_item(request):
    if request.method == 'POST':
        form = StuffForm(request.POST, request.FILES)
        if form.is_valid():
            new_item = form.save()

            stuff_added_signal.send(sender=Stuff, stuff=new_item)

            return redirect('index')

    else:
        form = StuffForm()

    context = {'form': form}
    return render(request, 'add_item.html', context)
