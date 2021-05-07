from django.db import models
from store.models.product import Product
from store.models.customer import Customer
import datetime
class Orders(models.Model):
    product= models.ForeignKey("Product", on_delete=models.CASCADE)
    customer= models.ForeignKey("Customer", on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
    price=models.IntegerField()
    date=models.DateField(default=datetime.datetime.today())
    address = models.CharField(max_length=50,default='',blank=True)
    phone = models.CharField(max_length=50,default='',blank=True)
    status = models.BooleanField(default=False)
    
    
    def place_order(self):
        self.save()
        
    @staticmethod
    def get_order_by_customerId(customerID):
        return Orders.objects.filter(customer = customerID ).order_by('-date')