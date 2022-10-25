from django.contrib import admin
from .models import Product, Order, Profile
from django.contrib.auth.models import Group
# Register your models here.

admin.site.site_header ="FliqInventory Dashboard" #changes admin-panel title

class ProductAdmin(admin.ModelAdmin):
    list_display = ('category','quantity')   #displays items in specific list

admin.site.register(Product, ProductAdmin)
admin.site.register(Order)
admin.site.unregister(Group)
admin.site.register(Profile)