from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify
#from .models import Terapeuta, Album, Photo
#from files.apps.amazura.apps import AmazuraConfig
import random



def terapeuta_pre_save(sender, **kwargs):
    print("calling terapeuta")
    terapeuta = kwargs.get('instance')
    if not terapeuta.code:
        terapeuta.code = slugify("{0}{1}{2}".format(terapeuta.first_name, terapeuta.last_name, random.randrange(10, 100)))

    if not terapeuta.slug:
        terapeuta.slug = '-'.join((slugify(terapeuta.first_name), slugify(terapeuta.last_name)))

    print(terapeuta.slug, terapeuta.code)



def album_pre_save(sender, **kwargs):
    album = kwargs.get('instance')

    if not album.code:
        album.code = slugify("{0}{1}{2}".format(album.terapeuta.code, album.title, random.randrange(100, 1000)))

    if not album.slug:
        album.slug = slugify(album.title)

    print(album.slug, album.code)



def photo_pre_save(sender, **kwargs):
    foto = kwargs.get('instance')

    if not foto.code:
        foto.code = slugify("{0} {1}".format(foto.album.code, random.randrange(999, 99999)))
    print(foto.code)