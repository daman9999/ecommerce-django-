from django.shortcuts import render , redirect
from django.contrib.auth.hashers import check_password
from store.models.product import Product
from store.models.category import Category
from store.models.customer import Customer
from store.models.orders import Orders
from django.http import HttpResponse
from django.views import View




class OrderView(View):
    
    def get(self,request):
        customer=request.session.get('customer_id')
        orders = Orders.get_order_by_customerId(customer)
        print(f"orders are:{orders}")
        return render(request,'orders.html',{'orders':orders})
    