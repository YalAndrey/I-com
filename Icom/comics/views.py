from django.shortcuts import render
from .models import Comics


def comics(request):
    com = Comics.objects.all()
    return render(request, 'Comics/comics.html', {'com': com})