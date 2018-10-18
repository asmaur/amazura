from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "amazura/coming.html")

def error_404_view(request, exception):
    return render(request,'amazura/error.html', {}, status=404)

def error_403_view(request, exception):
    return render(request,'amazura/error.html', {}, status=403)

def error_500_view(request, exception):
    return render(request,'amazura/error.html', {}, status=500)