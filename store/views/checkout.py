from django.shortcuts import render , redirect
from django.contrib.auth.hashers import check_password
from store.models.product import Product
from store.models.category import Category
from store.models.customer import Customer
from django.http import HttpResponse
from django.views import View
from store.models.orders import Orders



class CheckOut(View):
    
    def post(self,request):
        address=request.POST.get('address')
        phone=request.POST.get('phone')
        customer=request.session.get('customer_id')
        print(f"session cstme{customer}")        
        cart=request.session.get('cart')        
        products=Product.get_all_products_by_Id(list(cart.keys()))
        for product in products:
            order=Orders(
                product=product, customer = Customer(id=customer), quantity=cart.get(str(product.id)), price=product.price, address=address, phone=phone,
            )
        
        
        order.save()
        request.session['cart']={}
        return redirect('cart')
   
    
    
