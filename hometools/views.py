from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from phone import views as vp
from .models import ProductDetails, Product
from phone.models import Cart

# Create your views here.

def showproduct(request):
    template = loader.get_template('showproduct.html')
    appliances = ProductDetails.objects.select_related('productid')
    context={'appliances':appliances, 'request':request}
    return HttpResponse(template.render(context))


def detailsproduct(request , id):
     template=loader.get_template('detailsHome.html')
     appliances=ProductDetails.objects.select_related('productid').filter(id=id)
     context={'appliances':appliances, 'request':request}
     return HttpResponse(template.render(context))


def add_to_cart(requset,id):
     currentuser=requset.user
     discount=2
     state=False
     phone=ProductDetails.objects.select_related('productid').filter(id=id)
    
     for item in phone:
           net=item.total-discount
     cart = Cart(
      Id_product=item.id,
      Id_user=currentuser.id,
      price=item.price,
      qty=item.qty,
      tax=item.tax,
      total=item.total,
      discount=discount,
      net=net,
      status=state
)
     

     currentuser=requset.user.id
     count=Cart.objects.filter(Id_user=currentuser).count()
     print(count)
     cart.save()
     requset.session['countcart']=count
     return redirect("/showproduct")