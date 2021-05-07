from django.contrib import admin
from django.urls import path
from .views.Login import Login
from .views.Signup import Signup
from .views.Login import logout
from .views.home import Index
from .views.cart import Cart
from .views.orderview import OrderView
from .views.checkout import CheckOut
from .middlewares.auth import auth_middleware
from .views.ErrorViewFile import ErrorView
from . import views
urlpatterns = [
    path('',Index.as_view(),name='index'),
    path('signup' ,Signup.as_view() ,name='signup'),
    path('signin' ,Login.as_view() ,name='signin'),
    path('logout' ,logout ,name='logout'),
    path('cart' ,Cart.as_view() ,name='cart'),
    path('checkout' ,CheckOut.as_view() ,name='checkout'),
    path('cartEmpty' ,ErrorView.as_view() ,name='cartEmpty'),
    path('orders' ,auth_middleware(OrderView.as_view()),name='orders'),
]
