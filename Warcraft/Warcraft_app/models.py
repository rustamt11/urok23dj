from django.db import models


# Create your models here.

class Video(models.Model):
    name = models.CharField(max_length=100)
    categorys = (("Cinematic", 'Синематики'), ("GameProcess", 'Игровой Процесс'))
    category = models.CharField(max_length=20, choices=categorys)
    video = models.FileField(upload_to='videos/')

    def __str__(self):
        return self.name


class Audio(models.Model):
    name = models.CharField(max_length=100)
    categorys = (("Music", 'Музыка'), ("Replicas", 'Реплики'))
    category = models.CharField(max_length=20, choices=categorys)
    audio = models.FileField(upload_to='audios/')

    def __str__(self):
        return self.name
