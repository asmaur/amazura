from django.shortcuts import render, HttpResponse, redirect, get_object_or_404, Http404

import datetime
from django.conf import settings
from .models import (Terapeuta, Album, Photo)

# Create your views here.

def set_cookies(response, key, value, days_expire = 30):
    if days_expire is None:
        max_age = 365 * 24 * 60 * 60  # one year
    else:
        max_age = days_expire * 24 * 60 * 60
    expires = datetime.datetime.strftime(datetime.datetime.utcnow() + datetime.timedelta(seconds=max_age),
                                         "%a, %d-%b-%Y %H:%M:%S GMT")
    response.set_cookie(key, value, max_age=max_age, expires=expires, domain=settings.SESSION_COOKIE_DOMAIN,
                        secure=settings.SESSION_COOKIE_SECURE or None)


def check_cookies(request):
    if 'allowed' in request.COOKIES and request.COOKIES['allowed'] == "true":
        return True

def index(request):
    if check_cookies(request):
        #terapeutas = Terapeuta.objects.all()
        return render(request, "amazura/index.html",) #{"teras" : terapeutas})
    else:
        return redirect("/")


def contato(request):

    if check_cookies(request):
        #terapeutas = Terapeuta.objects.all()
        return render(request, "amazura/contato.html",) #{"teras" : terapeutas})

    else:
        return redirect("/")

def init(request):
    if check_cookies(request):
        return redirect("/inicio")
    else:
        msg = "Algo deu errado, tente novamente mais tarde."
        if request.method == "POST":
            print(request.POST['allowed'])
            if request.POST['allowed'] == "true":
                try:
                    response = redirect("/inicio")
                    set_cookies(response, "allowed", "true")
                    return response
                except KeyError:
                    msg = "Habilite os cookies e tente novamente"
                    return render(request, "amazura/init.html", {"msg": msg})
            else:

                return render(request, "amazura/init.html", {"msg": msg})

    return render(request, "amazura/init.html")


def page(request, slug, id):
    if check_cookies(request):
        terapeutas = Terapeuta.objects.all()
        terapeuta = get_object_or_404(Terapeuta, pk=int(id))
        albuns = Album.objects.filter(terapeuta__pk=int(id))

        photos = Photo.objects.all().filter(album__in=albuns)
        return render(request, "amazura/page.html", {"teras" : terapeutas, "tera": terapeuta, 'photos':photos})
    else:
        redirect("/")

def valores(request):
    if check_cookies(request):
        #terapeutas = Terapeuta.objects.all()
        return render(request, "amazura/valores.html",)# {"teras" : terapeutas})
    else:
        redirect("/")


def salazar(request,):
    if check_cookies(request):
        return render(request, "amazura/salazar.html",)
    else:
        redirect("/")

def muniz(request,):
    if check_cookies(request):
        return render(request, "amazura/muniz.html",)
    else:
        redirect("/")

def amorim(request,):
    if check_cookies(request):
        return render(request, "amazura/amorim.html",)
    else:
        redirect("/")

def rodriguez(request,):
    if check_cookies(request):
        return render(request, "amazura/rodriguez.html",)
    else:
        redirect("/")



def error_404_view(request, exception):
    return render(request,'amazura/error.html', {}, status=404)

def error_403_view(request, exception):
    return render(request,'amazura/error.html', {}, status=403)

def error_500_view(request, exception):
    return render(request,'amazura/error.html', {}, status=500)





