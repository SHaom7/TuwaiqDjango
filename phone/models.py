from django.db import models

# Create your models here.


class Items(models.Model):
    name=models.CharField(max_length=50)
    def __str__(self):
        return self.name

class ItemDetails(models.Model):
    color=models.CharField(max_length=50)
    price=models.FloatField()
    qty=models.IntegerField()
    tax=models.FloatField()
    total=models.FloatField()
    image=models.CharField(max_length=50, null=True)
    date=models.DateTimeField(auto_now_add=True)
    itemsid=models.ForeignKey(Items, on_delete= models.CASCADE) #to estblish the one to many relation where ecah name could take more than one record 
    def __str__(self):
        return self.itemsid