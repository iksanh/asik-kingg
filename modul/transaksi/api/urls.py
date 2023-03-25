from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from modul.transaksi.api import view


urlpatterns = [
    path('akun/', view.AkunList.as_view()),
    path('akun/<int:pk>/', view.AkunDetail.as_view()),

    path('angsuran/', view.AngsuranList.as_view()),
    path('ansurang/<int:pk>/', view.AngsuranDetail.as_view())
]