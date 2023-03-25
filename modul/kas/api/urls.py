from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from modul.kas.api import view


urlpatterns = [
    path('kas/', view.KasList.as_view()),
    path('kas/<int:pk>/', view.KasDetail.as_view())
]