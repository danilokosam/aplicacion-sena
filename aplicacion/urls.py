"""
URL configuration for aplicacion project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
# from django.contrib.auth.views import LoginView
from . import views

urlpatterns = [
    path('django-admnistracion/', admin.site.urls),
    path('admin/', views.index_admin, name='index-admin'),
    path('user/', views.index_user, name='index-user'), # <-- Pendiente de revision
    path('', views.index, name='index'),
    
    path('usuarios/', include('usuarios.urls')),
    path('usuarios/api/', include('usuarios.api_urls')),
    path('servicios/', include('servicios.urls')),
    path('servicios/api/', include('servicios.api_urls')),
    path('productos/', include('productos.urls')),
    
    path('login/', views.MyLoginView.as_view(), name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('', include('django.contrib.auth.urls')),
    path('serviciosuser/', views.serviciosuser, name='servicios user'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
