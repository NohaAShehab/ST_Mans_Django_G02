from django.shortcuts import render, redirect
from categories.models import Category
from django.http import HttpResponse
# Create your views here.

def categories_index(request):
    categories =Category.get_all_categories()
    return render(request, "categories/index.html", context={"categories":categories})


def category_show(request, id):
    category = Category.get_category_object(id)
    # return HttpResponse(category)
    return render(request, "categories/show.html", context={"category":category})


def category_create(request):
    if request.POST:
        category = Category()
        category.cat_name= request.POST["cat_name"]
        if request.FILES:
            category.image = request.FILES["image"]

        category.save()
        return redirect(Category.get_index_url())

    return render(request, "categories/create.html")



def category_edit(request, id):
    category = Category.get_category_object(id)
    if request.POST:
        category.cat_name = request.POST["cat_name"]
        if request.FILES:
            category.image = request.FILES["image"]

        category.save()
        return redirect(Category.get_index_url())

    return  render(request, "categories/edit.html", context={"category":category})



def category_delete(request, id):
    category = Category.get_category_object(id)
    category.delete()
    return redirect(Category.get_index_url())

