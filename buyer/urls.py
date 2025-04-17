from django.urls import path
from . import views
urlpatterns = [

    path('',views.home,name='home'),
    path('newbuyer/',views.newbuyer,name='newbuyer'),
    path('updatebuyer/',views.updatebuyer,name='updatebuyer'),
    path('deletebuyer/<int:id>',views.deletebuyer,name='deletebuyer'),
    path('buyerdetails/',views.buyerdetails,name='buyerdetails'),
    path('contact/',views.contact,name='contact'),
    #path('messages/',views.all_messages,name='messages'),
]
