from django.shortcuts import render
from django.views.generic import TemplateView, View
from home.models import Product, Product_categories, Option, User, Customer
from register.models import *
import os
from order.models import *
from django.views.generic import ListView
def get_home(request, page = 0):
    login_status = request.user.is_authenticated
    name = request.user.username
    if login_status:
        cart = Cart.objects.filter(user_id=request.user.id).last()
        if cart != None :
            count = cart.products.count
        else:
            count = 0
    else:
        count = 0
    product = Product.objects.all()
    if len(product) > 20:
        product = product[page*20:(page+1)*20]
    login_status = request.user.is_authenticated
    context= {
        'product' : product,
        'login_status' : login_status,
        'count' : count,
        'name' : name
    }
    return render(request, 'Ecommerce-Template-Bootstrap-master/product.html', context)


def get_product(request, id):
    login_status = request.user.is_authenticated
    name = request.user.username

    if login_status:
        cart = Cart.objects.filter(user_id=request.user.id).last()
        if cart != None :
            count = cart.products.count
        else:
            count = 0
    else:
        count = 0
    product = Product.objects.get(pk = id)
    context= {
        'product' : product,
        'login_status' : login_status,
        'count' : count,
        'name' : name
    }
    return render(request, 'Ecommerce-Template-Bootstrap-master/comment.html', context)



def get_product_by_category(request, category, page = 0):
    name = request.user.username

    login_status = request.user.is_authenticated
    if login_status:
        cart = Cart.objects.filter(user_id=request.user.id).last()
        if cart != None :
            count = cart.products.count
        else:
            count = 0
    else:
        count = 0
    product = Product.objects.filter(categories__categories_Name = category)
    product = product[page*20:(page+1)*20]
    login_status = request.user.is_authenticated
    context= {
        'product' : product,
        'page':page,
        'login_status': login_status,
        'count' : count,
        'name' : name
    }
    return render(request, 'Ecommerce-Template-Bootstrap-master/product.html', context)


def search(request, search_content, page = 0):
    login_status = request.user.is_authenticated
    product = Product.objects.filter(prduct_name__icontains=search_content)
    no_result = product.__len__() == 0
    if len(product) > 20:
        product = product[page*20:(page+1)*20]
    context= {
        'product' : product,
        'login_status' : login_status,
        'no_result': no_result,

    }
    return render(request, 'Ecommerce-Template-Bootstrap-master/search-page.html', context)
