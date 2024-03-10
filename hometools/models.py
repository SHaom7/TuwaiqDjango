from django.db import models

# Create your models here.

class Product(models.Model):
 name=models.CharField(max_length=50)
 def __str__(self):
        return self.name

class ProductDetails(models.Model):
 brand=models.CharField(max_length=50, null=True)
 des=models.CharField(max_length=150, null=True)
 color=models.CharField(max_length=50)
 price=models.FloatField()
 qty=models.IntegerField()
 tax=models.FloatField()
 image=models.CharField(max_length=150)
 total=models.FloatField()
 date=models.DateTimeField(auto_now_add=True)
 productid=models.ForeignKey(Product,on_delete=models.CASCADE,null=True)
def __str__(self):
        return self.price