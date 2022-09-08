from django.db import models
from categories.models import Category
from django.shortcuts import reverse
# Create your models here.

class Product(models.Model):
    ## add the basic properties to class
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=10)
    description = models.CharField(max_length=1000)
    # image = models.CharField(max_length=100)
    image =  models.ImageField(upload_to="products/images", null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at=  models.DateTimeField(auto_now=True, null=True)
    category = models.ForeignKey(Category, null=True, on_delete=models.CASCADE,
                                 related_name='cat_products') # create column cat_id, reference table categories(id)

    def __str__(self):
        return self.name


    def get_image_url(self):
        return f"/media/{self.image}"

    def get_show_url(self):
        return reverse("products_show", args=[self.id])