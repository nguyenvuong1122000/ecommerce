from django import forms
from django.forms import Form
from order.models import Order
import datetime

class Check_outForm(Form):
    name = forms.CharField(max_length=200)
    email = forms.EmailField(max_length=200)
    address1 = forms.CharField(max_length=200)
    phone_number = forms.CharField(max_length=11)

    def create_order(self, seller_id,  product_query_set ):

        last = Order.objects.order_by("-order_ID")
        if last.exists():
            id = last[0].order_ID + 1
            print("id la {}".format(id))
        else:
            id = 0
        order = Order(seller_ID_id = seller_id, creation_date=datetime.datetime.now(), order_ID= id)
        order.name = self.data['name']
        order.address1 = self.data['address1']
        order.email = self.data['email']
        order.phone_number = self.data['phone_number']
        order.save()

        order.add_product_query_set(product_query_set)


