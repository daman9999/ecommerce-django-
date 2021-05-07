from django.shortcuts import render , redirect
from django.contrib.auth.hashers import check_password
from store.models.product import Product
from store.models.category import Category
from store.models.customer import Customer
from django.http import HttpResponse
from django.views import View
from store.models.product import Product
class Cart(View):
    
    def get(self,request):
        if not (request.session.get('cart')):
            return redirect('cartEmpty')
        else:    
            ids = list(request.session.get('cart').keys())
            products=Product.get_all_products_by_Id(ids)
            print(products)
            return render(request,'cart.html',{'products':products})
        
