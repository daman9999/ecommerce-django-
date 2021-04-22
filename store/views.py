from django.shortcuts import render
from .models.product import Product
from .models.category import Category
# Create your views here.

def index(request):
    products= None
    categoryID = request.GET.get('category')
    categories=Category.get_all_categories()
    print(categoryID)
    if categoryID:
        products=Product.get_all_products_by_categoryId(categoryID)
        print(products)
    else:
        products=Product.get_all_products()
    data={}
    data['products'] = products
    data['category'] = categories
    return render(request,'index.html',data)

def signup(request):
    return render(request,'signup.html')
