from django.urls import include, re_path, path

from .views import *



urlpatterns = [
    re_path(r'^$',init),
    re_path(r'^inicio',index),
    re_path(r'^contato$',contato),

]