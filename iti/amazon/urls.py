from django.urls import path
from amazon.views import homepage, helloWorld, welcome, contactus, homepageview, \
    profileview, allproductsView, showproduct

urlpatterns = [
    path('home', homepage),
    path('hello', helloWorld),
    ## home/noha ---> argumented url
    path("welcome/<username>",welcome),
    path("contact",contactus),
    path("homepage",homepageview),
    path("profile/<name>",profileview ),
    path("amazonproducts", allproductsView, name='all_amazon_products'),
    path("amazonproducts/<int:product_id>",showproduct, name ='show_amazon_product')
]
