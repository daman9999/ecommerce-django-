from django.shortcuts import render , redirect
from django.contrib.auth.hashers import make_password ,check_password
from store.models.product import Product
from store.models.category import Category
from store.models.customer import Customer
from django.http import HttpResponse
from django.views import View


class Signup(View):
    def validateCustomer(self,customer,error):
        error_message = ''
        if (not customer.first_name):
            error_message =error_message+ "First Name Required !!\n"
        elif len(customer.first_name) < 4:
            error_message = error_message +'First Name must be 4 char long or more\n'
        elif not customer.last_name:
            error_message = error_message +'Last Name Required\n'
        elif len(customer.last_name) < 4:
            error_message = error_message +'Last Name must be 4 char long or more\n'
        elif not customer.phone:
            error_message = error_message +'Phone Number required\n'
        elif len(customer.phone) < 10:
            error_message = error_message +'Phone Number must be 10 char Long\n'
        elif len(customer.password) < 6:
            error_message = error_message +'Password must be 6 char long\n'
        elif len(customer.email) < 5:
            error_message = error_message +'Email must be 5 char long\n'
        elif customer.isExist():
            error_message = error_message +'Email Address Already Registered..\n'
        return error_message
    
    
    def get(self,request):
        return render(request,'signup.html')
    
    def post(self,request):
        postData = request.POST
        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        phone = postData.get('phone')
        email = postData.get('email')
        password = postData.get('password')
        customer =Customer(
            first_name= first_name,
            last_name= last_name ,
            phone= phone , 
            email= email ,
            password= password,
            )#pass to customer model        
        
        #passing values while validation
        values={
            "first_name":first_name,
            "last_name": last_name ,
            "phone":phone , 
            "email": email ,
        }
        #validation
        error=None
        error= self.validateCustomer(customer,error)
        print(error)
        if not error:    
            customer.password=make_password(customer.password)
            customer.register() #saving the customer data
            return redirect('index')            
        else :
            datas={
                'error':error,
                'values':values
            }     
            print('entered')
            return render(request,'signup.html',datas)

    

    
