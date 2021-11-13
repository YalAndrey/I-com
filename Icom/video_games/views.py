from django.shortcuts import render
from .models import Video_games


def video_games(request):
    vi_ga = Video_games.objects.all()

    ci = []
    c2 = []
    for i in vi_ga:
        ci += [i] * 5
        if len(ci) == 5:
            c2 += [ci] * 5
            ci = []
    c2.append(ci)
    return render(request, 'Video_game/video_games.html', {'vi_ga': c2})


def game(request, id_game):
    com = Video_games.objects.all()
    n = None
    for i in com:
        if i.id == id_game:
            n = i
    n.trailer = '//www.youtube.com/embed/' + n.trailer.split('watch?v=')[-1]
    li = [1, 2, 3, 4, 5]
    return render(request, 'Video_game/game.html', {'game': n, 'li': li})