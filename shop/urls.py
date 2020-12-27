from django.urls  import path
from . import views 


urlpatterns = [
    path('',views.home,name='Shophome'),
    path('about/',views.about,name='AboutUs'),
    path('contact',views.contact,name='ContactUs'),
    path('search',views.search,name='Search'),
    path('productView/<int:myid>',views.prodview,name='ProductView'),
    path('tracker',views.track,name='Tracker'),
    path('checkout',views.check,name='Checkout'),
   
    
]