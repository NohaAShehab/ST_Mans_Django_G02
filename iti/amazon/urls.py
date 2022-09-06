from django.urls import path
from amazon.views import homepage, helloWorld, welcome, contactus, homepageview, profileview

urlpatterns = [
    path('home', homepage),
    path('hello', helloWorld),
    ## home/noha ---> argumented url
    path("welcome/<username>",welcome),
    path("contact",contactus),
    path("homepage",homepageview),
    path("profile/<name>",profileview )
]
