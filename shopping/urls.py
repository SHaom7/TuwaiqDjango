from django.contrib import admin
from django.urls import path
from phone import views
from phone_api import views as v1
from hometools import views as v2

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('showphone/',views.showphone,name='showphone'),
    path('details/<int:id>/',views.details,name='details'),
    path('auth_register/',views.auth_register,name='auth_register'),
    path('auth_login/',views.auth_login,name='auth_login'),
    path('auth_logout/',views.auth_logout,name='auth_logout'),
    path('checkout/',views.checkout,name='checkout'),
    path('add_to_cart/<int:id>/',views.add_to_cart,name='add_to_cart'),
    path('api/itemlist/all',v1.getallitems_list,name='itemall'),
    path('api/list_item_details/details',v1.list_item_details,name='details'),
    path('api/list_item_detailsbyid/details/<int:id>/',v1.list_item_detailsbyid,name='detailsbyid'),
    path('showproduct/', v2.showproduct, name='showproduct'),
    path('detailsP/<int:id>/',v2.detailsproduct,name='detailsproduct'),

    
]
