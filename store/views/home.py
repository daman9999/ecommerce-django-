from django.shortcuts import render , redirect,HttpResponseRedirect
from django.contrib.auth.hashers import make_password ,check_password
from store.models.product import Product
from store.models.category import Category
from store.models.customer import Customer
from django.http import HttpResponse
from django.views import View
# Create your views here.


class Index(View):
    def post(self , request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        # je cart mili te initialize kro session
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(product)
                    else:
                        cart[product]  = quantity-1
                else:
                    cart[product]  = quantity+1

            else:
                cart[product] = 1
        else:
            #je nahi mili te cart ban jaawe te ek product add ho jawe
            cart = {}
            cart[product] = 1

        request.session['cart'] = cart
        print('cart' , request.session['cart'])
        return redirect('index')
    
    
    def get(self,request):
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}
        products= None
        categoryID = request.GET.get('category')
        categories=Category.get_all_categories()
        if categoryID:
            products=Product.get_all_products_by_categoryId(categoryID)
        else:
            products=Product.get_all_products()
        data={}
        data['products'] = products
        data['category'] = categories
        return render(request,'index.html',data)


