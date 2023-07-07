#url for api
from django.urls import path, include

urlpatterns = [
    path('auth/', include('rest_framework.urls')),
    path('simpanan/', include('modul.simpanan.api.urls')),
    path('transaksi/', include('modul.transaksi.api.urls')),
    path('kas/', include('modul.kas.api.urls')),
]
