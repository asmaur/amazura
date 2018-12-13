from django.urls import include, re_path, path

from .views import *



urlpatterns = [
    re_path(r'^$',init),
    re_path(r'^inicio$',index),
    re_path(r'^contato$',contato),
    re_path(r'^valores$',valores),
    re_path(r'^photos/ivy-salazar$',salazar),
    re_path(r'^photos/carol-muniz$',muniz),
    re_path(r'^photos/laura-amorim$',amorim),
    re_path(r'^photos/livia-rodriguez$',rodriguez),
    #re_path(r'^photos/(?P<slug>[\w-]+)/(?P<id>\d+)$',page),

]