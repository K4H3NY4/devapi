from django.contrib import admin
from .models import Customer
from .models import Item
from .models import Order

# Register your l ls here.

admin.site.register(Customer)
admin.site.register(Item)
admin.site.register(Order)
