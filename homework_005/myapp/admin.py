from django.contrib import admin
from .models import Client, Item, Order

# Register your models here.

admin.site.register(Client)
admin.site.register(Item)
admin.site.register(Order)
