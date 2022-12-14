from django.shortcuts import render
from .astroid_builder import AsteroidBuilder

builder = None


# Create your views here.
def start(request):
    return render(request, "start.html")

def getCoords(request):
    global builder
    return builder.getAllCoordinates()

def home(request):
    global builder

    w = int(request.GET.get('w'))
    h = int(request.GET.get('h'))

    builder = AsteroidBuilder(size=3, h=h, w=w)
    return render(request, "home.html", context=builder.getAllCoordinates())
