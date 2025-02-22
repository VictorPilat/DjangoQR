from django.urls import path
from . import views
urlpatterns = [
    
    path('packet_pro/', views.render_packet_pro, name ='packet_pro' ),
    path('packet_standard/', views.render_packet_standard, name ='packet_standard' ),
   
]