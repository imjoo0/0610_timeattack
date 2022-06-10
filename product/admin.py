from django.contrib import admin
from .models import Product, ProductOrder, UserOrder,OrderStatus,Category

# Register your models here.

admin.site.register(Product)
admin.site.register(ProductOrder)
admin.site.register(Category)
admin.site.register(UserOrder)
admin.site.register(OrderStatus)