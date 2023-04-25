from django.urls import path, include
from modul.pinjaman  import views as view

urlpatterns = [
    path('', view.list_pinjaman, name = 'list-pinjaman'),
    path('create',  view.create_pinjaman, name='create-pinjaman'),
    path('edit/<int:id>', view.edit_pinjaman, name = 'edit-pinjaman'),
    path('delete/<int:id>', view.delete_pinjaman, name = 'delete-pinjaman')
]