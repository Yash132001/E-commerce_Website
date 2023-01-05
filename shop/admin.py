from django.contrib import admin
from . models import Product
from . models import Lightbil
from .models import Contact
from . models import Order
from .models import OrderUpdate



# Register your models here.

admin.site.register(Product)
admin.site.register(Lightbil)
admin.site.register(Contact)
admin.site.register(Order)
admin.site.register(OrderUpdate)

