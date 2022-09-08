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



def getAllproducts():
    products = [{'id':1, 'name':'product1', 'price':10, 'image':'product1.png'},
                {'id': 2, 'name': 'product2', 'price': 10, 'image': 'product2.png'},
                {'id': 3, 'name': 'product3', 'price': 10, 'image': 'product3.png'},
                {'id': 4, 'name': 'product4', 'price': 10, 'image': 'product4.png'}]
    return products

def allproductsView(request):
    products = getAllproducts()
    return render(request, "amazon/allproducts.html", context={"products":products})



def showproduct(request, product_id):
    allproducts = getAllproducts()
    for product in allproducts:
        # print(type(product_id), type(product["id"]))
        if product_id ==product["id"]:
            # return HttpResponse(product)
            return render(request, 'amazon/showproduct.html', context={"product":product})

    return HttpResponse(404)

