import django
import os
import pandas as pd
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ecommerce.settings")

import django
django.setup()
from home.models import *
from django.contrib.auth.models import User

none = Product_categories.objects.get_or_create(pk = 0)[0]
laptop = Product_categories.objects.get_or_create(pk = 1)[0]
smartphone = Product_categories.objects.get_or_create(pk = 2)[0]
camera = Product_categories.objects.get_or_create(pk = 3)[0]
table = Product_categories.objects.get_or_create(pk = 4)[0]

seller = User.objects.get(username="vuong")

def add_product(product_ID, prduct_name = "None", prduct_price = 0, product_imagepath= "None", product_update_date= "2000-12-20", categories = none, seller = seller):
    if product_ID is None :
        print("product cant not NULL")
        return
    product = Product(product_ID = product_ID,
                      prduct_name = prduct_name,
                      prduct_price = prduct_price,
                      product_imagepath= product_imagepath,
                      product_update_date = product_update_date,
                      categories=  categories,
                      seller = seller
                      )
    product.save()
def add_product_from_csv(filepath, categories):
    data = pd.read_csv(filepath, error_bad_lines=False)
    id, name, price, path, desciption = data['id'], data['name'], data['price'], data['thumbnail_url'], data['description']
    for i in range(1, data.__len__()):
        product = Product(product_ID= id[i],
                          prduct_name=name[i],
                          prduct_price= price[i],
                          product_imagepath=path[i],
                          product_update_date="2019-01-01",
                          categories = categories,
                          seller = seller,
                          product_desciption = desciption[i]
                          )
        product.save()

if __name__ == "__main__":
    add_product_from_csv("/home/vuong/PycharmProjects/online_learning/crawler/maytinhbang.csv", table)
    add_product_from_csv("/home/vuong/PycharmProjects/online_learning/crawler/dienthoai.csv", smartphone)
    add_product_from_csv("/home/vuong/PycharmProjects/online_learning/crawler/laptop.csv", laptop)
    add_product_from_csv("/home/vuong/PycharmProjects/online_learning/crawler/mayanh.csv", camera)