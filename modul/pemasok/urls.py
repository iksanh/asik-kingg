from django.urls import path
from .views import PemasokView, PemasokCreate, PemasokUpdate, delete_pemasok

urlpatterns = [
  path('', PemasokView.as_view(template_name='pemasok/list_pemasok.html'), name='list-pemasok'),
  path('create/', PemasokCreate.as_view(template_name='pemasok/create_pemasok.html'), name='create-pemasok'),
  path('update/<int:pk>', PemasokUpdate.as_view(template_name='pemasok/create_pemasok.html'), name='edit-pemasok'),
  path('delete/<int:pk>', delete_pemasok, name='delete-pemasok')
]