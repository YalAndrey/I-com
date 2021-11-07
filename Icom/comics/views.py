from django.shortcuts import render
from .models import Comics


def comics(request):
    com = Comics.objects.all()
    ci = []
    c2 = []
    for i in com:
        ci.append(i)
        if len(ci) == 5:
            c2.append(ci)
            ci = []
    c2.append(ci)
    print(c2)
    return render(request, 'Comics/comics.html', {'com': c2})