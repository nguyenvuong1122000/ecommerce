from django.db import models
import os
from home.models import *
import os, django

class Cart(models.Model):
    cart_id = models.IntegerField(primary_key=True,null = False, auto_created= True, unique = True)
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)

    def add_to_cart(self, product_id):
        product = Product.objects.get(pk = product_id)
        self.products.add(product)
    def remove_from_cart(self, product_id):
        product = Product.objects.get(pk = product_id)
        self.products.remove(product)
    def __unicode__(self):
        return unicode(self.cart_id)

class Order(models.Model):
    order_ID = models.IntegerField(primary_key=True, auto_created=True, null = False, unique=True)
    seller_ID = models.ForeignKey(User, on_delete = models.CASCADE)
    creation_date = models.DateField(auto_now=True)
    is_end = models.BooleanField(default=False)

    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    address1 = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=11)

    products = models.ManyToManyField(Product)

    def add_product_query_set(self, product_set ):
        for pr in product_set:
            self.products.add(pr)

    class Meta:
        ordering = ('-creation_date',)
    def __str__(self):
        return self.order_ID.__str__()
    def address(self):
        return self.address1

class CountProduct(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    count = models.IntegerField(default=1)
