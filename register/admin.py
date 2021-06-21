import requests
from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from home.models import Product, Product_categories
from guardian.shortcuts import assign_perm
from django import forms
from django.utils.html import format_html


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    readonly_fields = [
        'product_ID',
    ]
    list_display = ["__str__", "COUNT"]
    actions = []

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        user = request.user
        return qs if user.is_superuser else qs.filter(seller_id=user.id)

    def COUNT(self, obj):
        request = getattr(self, 'request', None)
        return format_html(
            '<span>{}</span>',
            obj.cout
        )
    def get_changeform_initial_data(self, request):
        super().get_queryset(request)
        return {'seller' : request.user.id}
    fields = ["prduct_name",
              "prduct_price",
              "product_imagepath",
              "product_update_date",
              "product_desciption",
              "cout",
              "categories",
              "seller"
              ]


#option product here
    def add_option(self, request, queryset):
        pass


#
@admin.register(Product_categories)
class Product_categoriesAdmin(admin.ModelAdmin):
    pass

