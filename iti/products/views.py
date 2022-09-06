from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def proudctsHome(request):
    return HttpResponse("<h1> Products Home .... </h1>")


def contactus(request, name):
    return render(request, 'products/Contactus.html')