from django.urls import path
from products.views import proudctsHome, contactus

urlpatterns = [
    path("myproducts",proudctsHome),
    path("contact/<name>", contactus)
]
