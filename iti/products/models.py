from django.db import models

# Create your models here.

class Product(models.Model):
    ## add the basic properties to class
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=10)
    description = models.CharField(max_length=1000)
    image = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at=  models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name