from django.urls import path
from . import views
urlpatterns = [

    #path('',views.home),
    path('newproduct/',views.newproduct,name='newproduct'),
    path('updateproduct/<int:id>',views.updateproduct,name='updateproduct'),
    path('deleteproduct/<int:id>',views.deleteproduct,name='deleteproduct'),
    path('detailsproduct/',views.detailsproduct,name='detailsproduct'),
    path('search/',views.search,name='search'),
]
