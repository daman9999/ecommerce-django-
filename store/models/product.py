from django.db import models
from .category import Category

# Create your models here.
class Product(models.Model):
    
    name=models.CharField(max_length=50)
    price=models.IntegerField(default=0)
    category=models.ForeignKey(Category, on_delete=models.CASCADE,default=1)
    description=models.CharField( max_length=200,default="",null=True,blank=True)
    image=models.ImageField(upload_to='uploads//products/')
    
    @staticmethod
    def get_all_products():
        return Product.objects.all()
    
    @staticmethod
    def get_all_products_by_Id(list_of_ids):
        return Product.objects.filter(id__in = list_of_ids)
    
    @staticmethod
    def get_all_products_by_categoryId(categoryId):
        if categoryId:
            return Product.objects.filter(category=categoryId)
        else:
                return Product.get_all_products()