from django.urls import path
from modul.transaksi import views as view

urlpatterns = [
    path('', view.list_akun, name='akun'),
    path('create/', view.create_akun, name='create-akun'),
    path('edit/<int:id>', view.edit_akun, name='edit-akun'),
    path('delete/<int:id>', view.delete_akun, name='delete-akun')
]