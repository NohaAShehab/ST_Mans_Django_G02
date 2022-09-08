from django.shortcuts import render, reverse, redirect
from django.http import HttpResponse
# Create your views here.
from products.models import Product
from django.shortcuts import  get_object_or_404


def proudctsHome(request):
    return HttpResponse("<h1> Products Home .... </h1>")


def contactus(request, name):
    return render(request, 'products/Contactus.html')


def productsindexview(request):
    # get the data from the datbase
    allproducts = Product.objects.all()
    return  render(request, "products/index.html",context={"products":allproducts})

def showProduct(request, id):
    # product = Product.objects.get(pk=id)
    # if product:
    #     return render(request, 'products/show.html', context={"product":product})
    #
    # return HttpResponse("<h1>No such product 404 </h1>")
    product = get_object_or_404(Product, pk=id)
    return render(request, 'products/show.html', context={"product": product})


def createProduct(request):
    if request.POST:
        # return HttpResponse(request.POST["name"])
        # name = request.POST["name"]
        # price = request.POST["price"]
        # description = request.POST["description"]
        # image = request.POST["image"]
        ## use these data to create new object in the database
        product = Product()
        product.name= request.POST["name"]
        product.price = request.POST["price"]
        product.description = request.POST["description"]
        product.image = request.POST["image"]
        product.save()
        url =reverse("products_index")
        return redirect(url)

        # return HttpResponse("Product added ")

    return render(request, "products/create.html")




def deleteProduct(request, id):
    product= get_object_or_404(Product, pk=id)
    product.delete()
    url = reverse("products_index")
    return redirect(url)


def editProduct(request, id ):
    product = get_object_or_404(Product, pk=id)
    if request.POST:
        product.name = request.POST["name"]
        product.price = request.POST["price"]
        product.description = request.POST["description"]
        product.image = request.POST["image"]
        product.save()
        url = reverse("products_index")
        return redirect(url)

    return  render(request, "products/edit.html", context={'product':product})