from django.urls import path
from products.views import proudctsHome, contactus, \
    productsindexview, showProduct, createProduct, deleteProduct, editProduct

urlpatterns = [
    path("myproducts",proudctsHome),
    path("contact/<name>", contactus),
    path("index", productsindexview, name='products_index'),
    path("<int:id>", showProduct, name='products_show'),
    path("create", createProduct, name='products_create'),
    path("delete/<int:id>", deleteProduct, name='products_delete'),
    path("edit/<int:id>", editProduct, name='products_edit'),
]
