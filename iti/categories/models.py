from django.db import models
from django.shortcuts import get_object_or_404, reverse
# Create your models here.

class Category(models.Model):
    # # any column created by the models is not null by default --->
    cat_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="categories/images", null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)



    def __str__(self):
        return self.cat_name

    def get_image_url(self):
        return f"/media/{self.image}"

    @classmethod
    def get_all_categories(cls):
        return cls.objects.all()

    @classmethod
    def get_category_object(cls, id):
        return get_object_or_404(cls, pk=id)

    def get_show_url(self):
        return reverse("categories_show", args=[self.id])

    @classmethod
    def get_index_url(cls):
        return reverse("categories_index")

    def get_edit_url(self):
        return reverse("categories_edit", args=[self.id])

    def get_delete_url(self):
        return reverse("categories_delete", args=[self.id])