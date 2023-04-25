from django.urls import path, include
from modul.kas import views as view

urlpatterns = [

    path('', view.list_kas, name='list-kas'),
    path('create/', view.create_kas, name='create-kas'),
    path('edit/<int:id>', view.edit_kas, name='edit-kas'),
    path('delete/<int:id>', view.delete_kas, name='delete-kas')
]