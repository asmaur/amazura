from django.shortcuts import render, HttpResponse, redirect
import datetime
from django.conf import settings

# Create your views here.

def set_cookies(response, key, value, days_expire = 30):
    if days_expire is None:
        max_age = 30 #365 * 24 * 60 * 60  # one year
    else:
        max_age = days_expire #* 24 * 60 * 60
    expires = datetime.datetime.strftime(datetime.datetime.utcnow() + datetime.timedelta(seconds=max_age),
                                         "%a, %d-%b-%Y %H:%M:%S GMT")
    response.set_cookie(key, value, max_age=max_age, expires=expires, domain=settings.SESSION_COOKIE_DOMAIN,
                        secure=settings.SESSION_COOKIE_SECURE or None)


def index(request):
    if 'allowed' in request.COOKIES and request.COOKIES['allowed']=="true":
        return render(request, "amazura/index.html")
    else:
        return redirect("/")


def contato(request):
    if 'allowed' in request.COOKIES and request.COOKIES['allowed'] == "true":
        return render(request, "amazura/contato.html")
    else:
        return redirect("/")

def init(request):

    if 'allowed' in request.COOKIES and request.COOKIES['allowed'] == "true":
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


def error_404_view(request, exception):
    return render(request,'amazura/error.html', {}, status=404)

def error_403_view(request, exception):
    return render(request,'amazura/error.html', {}, status=403)

def error_500_view(request, exception):
    return render(request,'amazura/error.html', {}, status=500)

