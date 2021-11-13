from django.shortcuts import render
from .models import Comics
from .forms import FilterComicsForm


def comics(request):
    com = Comics.objects.all()
    if request.method == 'POST':
        form = FilterComicsForm(request.POST)
        if form.is_valid():
            marvel = form.cleaned_data.get('marvel')
            dc = form.cleaned_data.get('dc')
            dark_horse = form.cleaned_data.get('dark_horse')
            bubble = form.cleaned_data.get('bubble')
            other = form.cleaned_data.get('other')
            mark = form.cleaned_data.get('mark')
            com1 = []
            for comicse in com:
                if comicse.mark >= mark and ((
                        (comicse.isdatel == 'marvel' and marvel) or (comicse.isdatel == 'dark_horse' and dark_horse)
                        or (comicse.isdatel == 'dc' and dc) or (comicse.isdatel == 'bubble' and bubble) or (
                                comicse.isdatel == 'other' and other)) or all([not marvel, not dc, not bubble, not dark_horse, not other])):
                    com1.append(comicse)
            com = com1

    else:
        form = FilterComicsForm()

    ci = []
    c2 = []
    for i in com:
        ci.append(i)
        if len(ci) == 5:
            c2.append(ci)
            ci = []
    c2.append(ci)
    print(c2)
    return render(request, 'Comics/comics.html', {'com': c2, 'form': form})


def number(request, num):
    com = Comics.objects.all()
    n = None
    for i in com:
        if i.id == num:
            n = i
    print(n.json())
    li = [1, 2, 3, 4, 5]
    return render(request, 'Comics/number.html', {'nomer': n, 'li': li})
