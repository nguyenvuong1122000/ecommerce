import http

from django.shortcuts import render
from django.shortcuts import redirect
# Create your views here.
from django.contrib import messages
from django.shortcuts import render
from django.views.generic import TemplateView, View
from home.models import *
from order.models import *
from order.form import Check_outForm
from register.models import *
from django.http import HttpResponse, HttpResponseNotAllowed
import os

def checkout(request):
    return render(request, template_name="Ecommerce-Template-Bootstrap-master/checkout-page.html")

def add_to_cart(request):
    if request.method != 'POST':
        return HttpResponseNotAllowed(['POST'])
    product_id = request.POST.get('id')
    amount = request.POST.get('amount')

    if request.user.is_authenticated :
        try:
            cart = Cart.objects.filter(user_id=request.user.id).last()
            cart.add_to_cart(product_id)
            print("aaa")

        except :
            cart = Cart(user = Customer.objects.get(pk = request.user.id))
            cart.save()

            cart = Cart.objects.filter(user_id=request.user.id).last()
            cart.add_to_cart(product_id)

    return HttpResponse("return this string")

def remove_from_cart(request):
    if request.user.is_authenticated:
        product_id = request.body.decode('utf-8')
        print(product_id)

        cart = Cart.objects.filter(user=request.user).last()
        cart.remove_from_cart(product_id)

    return HttpResponse("return this string")


def check_out_page(request):
    login_status = request.user.is_authenticated
    cart = Cart.objects.filter(user_id=request.user.id).last()
    if cart is None:
        product_list = Product.objects.filter(cart= -1)
    else:
        product_list = Product.objects.filter(cart = cart.cart_id)
    status = False
    if product_list.exists():
        status = True
    total = 0

    for pr in product_list:
        total = total + pr.prduct_price

    seller_list = Product.objects.filter(cart = cart).values('seller_id')
    print(seller_list)
    if request.method == 'POST':
        form = Check_outForm(request.POST)
        if form.is_valid():
            for i, s in enumerate(seller_list):
                print(s['seller_id'])
                query_set = Product.objects.filter(cart = cart, seller_id= s['seller_id'])
                form.create_order(seller_id= s['seller_id'], product_query_set = query_set)
                print(query_set)
            cart = Cart(user=Customer.objects.get(pk=request.user.id))
            cart.save()
            return HttpResponse("Mua hàng thành công")
    else:
        form = Check_outForm()
    context = {
        "product_list" : product_list,
        "status" : status,
        "total" : total,
        "count" : len(product_list),
        "form" : form,
        "login_status" : login_status
    }
    return render(request, "Ecommerce-Template-Bootstrap-master/checkout-page.html", context= context)
