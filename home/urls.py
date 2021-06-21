from django.urls import path, re_path
from home.views import *
from home import views

urlpatterns = [
    path('', get_home, name='context'),
    path('product/<int:id>/', get_product),
    path('<str:category>/', get_product_by_category),
    path('<str:category>/page=<int:page>', get_product_by_category),
    path('search/<str:search_content>', search, name='search_results'),

]
