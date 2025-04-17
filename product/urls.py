from django.urls import path
from . import views
urlpatterns = [

    #path('',views.home),
    path('newproduct/',views.newproduct,name='newproduct'),
    path('updateproduct/<int:id>',views.updateproduct,name='updateproduct'),
    path('deleteproduct/<int:id>',views.deleteproduct,name='deleteproduct'),
    path('detailsproduct/',views.detailsproduct,name='detailsproduct'),
    path('search/',views.search,name='search'),

    path('checkout/',views.cart_view,name='checkout'),
    path('addtocart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.show_cart, name='show_cart'),
    path('removefromcart/<int:order_id>/', views.remove_from_cart, name='remove_from_cart'),
]
