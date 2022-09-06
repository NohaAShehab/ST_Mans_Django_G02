from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


### create my first view

def homepage(request):
    return HttpResponse("Hello World")


def helloWorld(request):
    return HttpResponse("<h1>Hello World </h1>")


def welcome(request, username):
    return HttpResponse(f" <h1 style='color:red; text-align:center' > Welcome {username} </h1>")


def contactus(request):
    return render(request, "amazon/Contactus.html")


def homepageview(request):
    return  render(request, "amazon/homepage.html")


def profileview(request, name):
    return render(request, "amazon/profile.html", context={"username":name})