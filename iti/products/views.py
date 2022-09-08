from django.shortcuts import render, reverse, redirect
from django.http import HttpResponse
# Create your views here.
from products.models import Product
from django.shortcuts import  get_object_or_404
from categories.models import Category

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
        product = Product()
        product.name= request.POST["name"]
        product.price = request.POST["price"]
        product.description = request.POST["description"]
        ## while creating the object you must pass the category object not the cat_id
        category = Category.get_category_object(request.POST["category_id"])
        product.category = category
        if(request.FILES):
            ## set its value to the object
            imagename = request.FILES["image"]
            product.image = imagename
            print(imagename, type(imagename))
        else:
            print("Image not found ")

        # product.image = request.POST["image"]  # this file object
        ## image information (request.FILES)
        # return HttpResponse("testtt")
        product.save()
        url =reverse("products_index")
        return redirect(url)

        # return HttpResponse("Product added ")

    # get the categories from the database ---> send it to the html page
    allcategories = Category.get_all_categories()
    return render(request, "products/create.html", context={"categories": allcategories})




def deleteProduct(request, id):
    product= get_object_or_404(Product, pk=id)
    image_url = product.get_image_url()
    ## delete the image
    # image_url.delete()
    product.delete()
    url = reverse("products_index")
    return redirect(url)


def editProduct(request, id ):
    product = get_object_or_404(Product, pk=id)
    if request.POST:
        product.name = request.POST["name"]
        product.price = request.POST["price"]
        product.description = request.POST["description"]
        category = Category.get_category_object(request.POST["category_id"])
        product.category = category
        if request.FILES:
            product.image = request.FILES["image"]

        product.save()
        url = reverse("products_index")
        return redirect(url)
    allcategories = Category.get_all_categories()

    return  render(request, "products/edit.html", context={'product':product,"categories":allcategories})