from django.urls import path
from modul.transaksi import views as view


urlpatterns = [
    path('', view.AkunView.as_view(), name='list-akun'),
    path('create/', view.create_akun, name='create-akun'),
    path('edit/<int:id>', view.edit_akun, name='edit-akun'),
    path('delete/<int:id>', view.delete_akun, name='delete-akun'),

    ## url for angsuran 
    path('angsuran/', view.AngsuranView.as_view(), name='list-angsuran'),
    path('create/angsuran', view.AngsuranCreate.as_view(), name='create-angsuran'),
    path('edit/angsuran/<int:pk>', view.AngsuranUpdate.as_view(), name='edit-angsuran'),
    path('delete/angsuran/<int:id>', view.angsuran_delete, name='delete-angsuran')

]