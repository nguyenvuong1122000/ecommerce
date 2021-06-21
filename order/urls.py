from django.urls import path, re_path
from order.views import *
from order import views
from django.conf.urls import url


urlpatterns = [
    path("checkout/", check_out_page, name = "checkout"),
    path("ajax/addtocart", add_to_cart, name = "add_to_cart"),
    path("ajax/rmproduct", remove_from_cart, name="remove_from_cart"),

]