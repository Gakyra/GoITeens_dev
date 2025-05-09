from django.shortcuts import render
from django.http import JsonResponse
from datetime import datetime

def clock_view(request):
    return render(request, 'clock.html')

def get_time(request):
    now = datetime.now().strftime('%H:%M:%S')
    return JsonResponse({'time': now})
