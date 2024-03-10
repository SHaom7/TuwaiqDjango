from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from phone import views as vp
from .models import ProductDetails, Product

# Create your views here.

def showproduct(request):
    template = loader.get_template('showproduct.html')
    appliances = ProductDetails.objects.select_related('productid')
    print(appliances.query)
    context={'appliances':appliances, 'request':request}
    return HttpResponse(template.render(context))


def detailsproduct(request , id):
     template=loader.get_template('details.html')
     currentuser=request.user
     print(currentuser.id)
     phone=ProductDetails.objects.select_related('productid').filter(id=id)
     context={
         'phone':phone,
         'request':request
     }
     return HttpResponse(template.render(context))