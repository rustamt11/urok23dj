from django.shortcuts import render
from django.views.generic import ListView

from Warcraft_app.models import Video, Audio


# Create your views here.

def index(request):
    return render(request, 'Warcraft_app/index.html')


def screenshots(request):
    context = {"numbers": range(1, 16)}
    return render(request, 'Warcraft_app/screenshots.html', context=context)


def about_the_game(request):
    return render(request, 'Warcraft_app/about_the_game.html')


class VideoListView(ListView):
    template_name = 'Warcraft_app/videos.html'
    model = Video
    context_object_name = 'video_list'


class AudioListView(ListView):
    template_name = 'Warcraft_app/audio.html'
    model = Audio
    context_object_name = 'audio_list'
