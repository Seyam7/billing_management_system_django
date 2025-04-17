from django.urls import path
from . import views
urlpatterns = [

    #path('',views.home),
    path('billpay/<int:id>',views.billpay,name='billpay'),
    path('checkout/',views.checkout,name='checkout'),
]
