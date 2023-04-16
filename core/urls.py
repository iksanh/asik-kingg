"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api-simpanan/', include('modul.simpanan.api.urls')),
    path('api-transaksi/', include('modul.transaksi.api.urls')),
    path('api-kas/', include('modul.kas.api.urls')),
    path('', include('modul.urls')),

    path('simpanan/', include('modul.simpanan.urls')),
    path('users/', include('modul.users.urls')),
    path('group/', include('modul.group.urls')),
    path('akun/', include('modul.transaksi.urls')),
    path('pinjaman/', include('modul.pinjaman.urls')),
    path('kas/', include('modul.kas.urls')),


]
