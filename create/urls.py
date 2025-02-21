from django.urls import path
from . import views
urlpatterns = [
    path('free/', views.render_free,name ='free' ),
    path('standard/', views.render_standard,name ='standard' ),
    path('pro/', views.render_pro,name ='pro' ),
]