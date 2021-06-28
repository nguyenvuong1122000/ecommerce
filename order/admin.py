from django.contrib import admin
from order.models import Order
# Register your models here.

def make_published(modeladmin, request, queryset):
    for order in queryset :
        order.is_end = True
        order.save()
make_published.short_description = 'Đánh dấu là đã giao hàng'


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["__str__", "address", "phone_number", "name"]
    actions = [make_published,]
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        user = request.user
        return qs if user.is_superuser else qs.filter(seller_ID_id=user.id)

