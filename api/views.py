from django.shortcuts import render
from rest_framework import viewsets
from .models import Customer
from .models import Item
from .models import Order
from .serializers import CustomerSerializer
from .serializers import ItemSerializer
from .serializers import OrderSerializer

# Create your views here.


class CustomerView(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class ItemView(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    
class OrderView(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


