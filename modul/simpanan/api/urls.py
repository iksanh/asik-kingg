from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from modul.simpanan.api import view


urlpatterns = [
    path('', view.SimpananList.as_view()),
    path('<int:pk>/', view.SimpananDetail.as_view())
]