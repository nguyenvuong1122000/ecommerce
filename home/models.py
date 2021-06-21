from django.db import models
from django.contrib.auth.models import User, Group
import os, django
# # # remove when runserver


class Product_categories(models.Model):
    categories_ID = models.IntegerField(primary_key=True, unique = True)
    categories_Name = models.CharField(max_length=200)
    def __str__(self):
        return f"{self.categories_Name}"

class Option(models.Model):
    OptionID = models.IntegerField()
    OptionName = models.CharField(max_length=200)

class Product(models.Model):
    product_ID = models.IntegerField(primary_key=True, auto_created= True, null = False, unique = True)
    prduct_name = models.CharField(max_length=200)
    prduct_price = models.IntegerField()
    product_imagepath = models.CharField(max_length= 400)
    product_update_date = models.DateField()
    product_desciption = models.CharField(max_length= 10000, default='NONE')
    cout = models.IntegerField(default=1)

    categories = models.ForeignKey(Product_categories, on_delete=models.CASCADE)
    seller = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.prduct_name}"
    def __byseller__(self):
        pass
class ProductOption(models.Model):
    ProductOption_ID = models.IntegerField(primary_key=True, auto_created= True, null = False, unique= True)
    Option_ID = models.ForeignKey(Option, on_delete= models.CASCADE)

    ProductID = models.ForeignKey(Product, on_delete= models.CASCADE)
    Option_Group_ID = models.IntegerField()


class Customer(User):
    def createOrder(self, request):
        pass
    def add_to_customer_group(self):
        self.groups.add(name = "Customer")

class Comment(models.Model):
    comment_ID = models.IntegerField(primary_key=True, auto_created=True)

    product_ID  = models.ForeignKey(Product,on_delete=models.CASCADE)
    user_ID  = models.ForeignKey(User,on_delete=models.CASCADE)
    context = models.CharField(max_length=2000)
    def __str__(self):
        return self.context