from rest_framework import serializers
from .models import Product

class CarSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('product_ID', 'prduct_name', 'prduct_price', 'product_imagepath', 'product_update_date', 'product_desciption', 'categories_ID', 'seller_ID')
