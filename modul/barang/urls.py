from django.urls import path
from .views import BarangCreate, BarangView, BarangUpdate, delete_barang
# from .views import 

urlpatterns = [
  path('', BarangView.as_view(template_name='barang/list_barang.html'), name='list-barang' ),
  path('create/', BarangCreate.as_view(template_name='barang/create_barang.html'), name='create-barang' ),
  path('edit/<int:pk>', BarangUpdate.as_view(template_name='barang/create_barang.html'), name='edit-barang' ),
  path('delete/<int:id>', delete_barang, name='delete-barang' ),
]