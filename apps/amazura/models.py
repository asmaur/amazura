from django.db import models
from django.utils.text import slugify
import random, os
from django.dispatch import receiver
from django.db.models.signals import pre_save
#from .signals import *

# Create your models here.


def photo_path_terapeuta(instance, filename):
# file will be uploaded to MEDIA_ROOT/company_<name>/
    return 'terapeutas_{0}_{1}/{2}'.format(instance.first_name, instance.last_name, filename)

def photo_path_album(instance, filename):
# file will be uploaded to MEDIA_ROOT/company_<name>/shop_<name>/
    parent_path = instance.album.terapeuta._meta.get_field('capa').upload_to(instance.album.terapeuta, '')
    return parent_path + 'album_{0}/{1}'.format(instance.album.title, filename)


def photo_path_bike(instance, filename):
    # file will be uploaded to MEDIA_ROOT/company_<name>/shop_<name>/bikes/
    parent_path = instance.shop._meta.get_field('photo').upload_to(instance.shop, '')
    return parent_path + 'bikes/{0}'.format(filename)

def get_code(instance):
    name1 = instance.terapeuta._meta.get_field('first_name')
    name2 = instance.terapeuta._meta.get_field('last_name')
    return "{0}{1}".format(name1[0], name2[0])


class TerapeutaManager(models.Manager):
    def get_queryset(self):
        return super(TerapeutaManager, self).get_queryset().filter(is_working=True)

class AlbumManager(models.Manager):
    def get_queryset(self):
        return super(AlbumManager, self).get_queryset().filter(is_visible=True)

class PhotoManager(models.Manager):
    def get_queryset(self):
        return super(PhotoManager, self).get_queryset().filter(is_public=True)

#Terapeutas

class Terapeuta(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    code = models.CharField(max_length=250, blank=True)
    created = models.DateField(auto_now_add=True)
    capa = models.ImageField(upload_to=photo_path_terapeuta)
    slug = models.SlugField( max_length=250, blank=True, default="")
    telefone = models.CharField(max_length=15,blank=True)
    peso = models.IntegerField(blank=True)
    altura = models.DecimalField(max_digits=3, decimal_places=2, blank=True)
    idade = models.IntegerField(blank=True)
    is_working = models.BooleanField(default=False)
    texto = models.TextField(default='')

    class Meta:
        ordering = ['created']
        verbose_name = "terapeuta"
        verbose_name_plural = "terapeutas"

    def __str__(self):
        return "{0} {1}".format(self.first_name,self.last_name)

    def fullname(self):
        return "{0} {1}".format(self.first_name,self.last_name)

    default = models.Manager()
    objects = TerapeutaManager()


#Albums

class Album(models.Model):
    title = models.CharField(max_length=50, default="comum")
    code = models.CharField(max_length=250, blank=True)
    terapeuta = models.ForeignKey('Terapeuta', related_name='albuns', verbose_name='terapeuta', on_delete=models.CASCADE, blank=True, null=True)
    is_visible = models.BooleanField( default=False)
    created = models.DateField(auto_now_add=True)
    slug = models.SlugField(max_length=250, blank=True, default="Comum")
    class Meta:
        ordering = ['-created']
        verbose_name_plural = 'albuns'

    def __str__(self):
        return self.code

    default = models.Manager()
    objects = AlbumManager()


#Photos

class Photo(models.Model):
    code = models.CharField(max_length=250, blank=True)
    image = models.ImageField(upload_to=photo_path_album)
    is_public = models.BooleanField(default=False)
    album = models.ForeignKey('Album', related_name='photos', verbose_name='album', on_delete=models.CASCADE, blank=True, null=True)
    valor = models.DecimalField(max_digits=3, decimal_places=2, default=5.69)
    date_added = models.DateTimeField('date added', auto_now_add=True)

    class Meta:
        ordering = ['-date_added']
        get_latest_by = 'date_added'
        verbose_name = "photo"
        verbose_name_plural = "photos"

    def __str__(self):
        return self.code

    default = models.Manager()
    objects = PhotoManager()



@receiver(pre_save, sender=Terapeuta)
def terapeuta_pre_save(sender, **kwargs):
    print("calling terapeuta")
    terapeuta = kwargs.get('instance')
    if not terapeuta.code:
        terapeuta.code = slugify("{0}{1}{2}".format(terapeuta.first_name, terapeuta.last_name, random.randrange(10, 100)))

    if not terapeuta.slug:
        terapeuta.slug = '-'.join((slugify(terapeuta.first_name), slugify(terapeuta.last_name)))

    print(terapeuta.slug, terapeuta.code)

@receiver(pre_save, sender=Album)
def album_pre_save(sender, **kwargs):
    album = kwargs.get('instance')

    if not album.code:
        album.code = slugify("{0}{1}{2}".format(album.terapeuta.code, album.title, random.randrange(100, 1000)))

    if not album.slug:
        album.slug = slugify(album.title)

    print(album.slug, album.code)


@receiver(pre_save, sender=Photo)
def photo_pre_save(sender, **kwargs):
    foto = kwargs.get('instance')

    if not foto.code:
        foto.code = slugify("{0} {1}".format(foto.album.code, random.randrange(999, 99999)))
    print(foto.code)