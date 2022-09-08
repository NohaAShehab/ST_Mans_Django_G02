

from django.urls import path, include
from categories.views import categories_index, category_show,\
    category_create, category_edit, category_delete
urlpatterns = [
    path("index", categories_index, name="categories_index"),
    path("<int:id>", category_show, name="categories_show"),
    path("create", category_create, name="categories_create"),
    path("edit/<int:id>", category_edit, name="categories_edit"),
    path("delete/<int:id>", category_delete, name="categories_delete"),

]
