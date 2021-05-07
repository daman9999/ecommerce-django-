from django.shortcuts import render
from django.views import View
# Create your views here.


class ErrorView(View):
    def get(self,request):
        return render(request,'Cart_not_found.html')