from django.apps import AppConfig
from django.db.models.signals import pre_save
from .models import *
from .signals import *

class AmazuraConfig(AppConfig):
    name = 'amazura'


"""
    label = 'mazura'
    def ready(self):
        pre_save.connect(terapeuta_pre_save, sender='Terapeuta')
        pre_save.connect(album_pre_save, sender='Album')
        pre_save.connect(photo_pre_save, sender='Photo')



class TerapeutaConfig(AppConfig):

    def ready(self):
        pre_save.connect(terapeuta_pre_save, sender=Terapeuta)

class AlbumConfig(AppConfig):

    def ready(self):
        pre_save.connect(album_pre_save, sender=Album)


class PhotoConfig(AppConfig):

    def ready(self):
        pre_save.connect(photo_pre_save, sender=Photo)

"""