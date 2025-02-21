
from django.urls import path
from . import views


urlpatterns = [
    path('log/',views.render_login, name = "login"),
    path('reg/',views.render_registr, name = "registr"),
]

