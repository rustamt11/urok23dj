from django.urls import path

from Warcraft_app.views import index, screenshots, about_the_game, VideoListView, AudioListView

urlpatterns = [
    path('', index, name='index'),
    path('screenshots/', screenshots, name='screenshots'),
    path('about_the_game/', about_the_game, name='about_the_game'),
    path('cinematics-videos/', VideoListView.as_view(), name='cinematics-videos'),
    path('audios/', AudioListView.as_view(), name='audios'),
]
