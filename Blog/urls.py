"""
URL configuration for Blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from home import render_home
from home_after import render_home_after
from my_qrcodes import render_my_qrcodes
from contact import render_contact
from login.views import logout_user
from django.conf import settings
from django.conf.urls.static import static


from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('img/favicon.ico'))),
    path('', render_home),
    path('home_after/', render_home_after, name='home_after'),
    # path('',include("home_after.urls"), name='home_after'),
    path('', include('login.urls'), name="login"),
    path('my_qrcodes/', render_my_qrcodes,name='my_qrcodes'),
    path('contact/', render_contact, name="contact"),
    path('',include("create.urls"), name='create'),
    path('logout/', logout_user, name = "logout")

    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
