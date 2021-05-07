from django.shortcuts import render , redirect,HttpResponseRedirect
from django.contrib.auth.hashers import check_password
from store.models.product import Product
from store.models.category import Category
from store.models.customer import Customer
from django.http import HttpResponse
from django.views import View




class Login(View):
    returnUrl=None
    def get(self,request):
        #'/orders' aa jana ithe from url
        Login.returnUrl=request.GET.get('return_url')
        print(Login.returnUrl)
        return render(request,'signin.html')
    
    def post(self,request):
        email=request.POST.get('email')
        password=request.POST.get('password')
        #write the error message
        error_message=None
        customer=Customer.get_customer_by_email(email)
        #return's matched email that email exits now check password
        if customer:
            flag = check_password(password,customer.password)
            if flag:
                request.session['customer_id'] = customer.id
                request.session['email'] = customer.email
                if Login.returnUrl:
                    #navigate to page by url
                    return HttpResponseRedirect(Login.returnUrl)
                else:
                    #next time lai
                    Login.returnUrl=None
                    return redirect('index')
            else:
                error_message='Email password does not exist'
                
        else:
            error_message='Email password does not exist'
        return render(request,'signin.html',{'error':error_message})
    
    
def logout(request):
    request.session.clear()
    return redirect('signin')