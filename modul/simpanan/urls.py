from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from modul.simpanan import  views as view


urlpatterns = [
    path('', view.list_simpanan, name = 'simpanan'),
    path('create/', view.create_simpanan, name = 'create-simpanan'),
    path('edit/<int:id>/', view.edit_simpanan, name = 'edit-simpanan'),
    path('delete/<int:id>/', view.delete_simpanan, name = 'delete-simpanan'),
    path('test', view.tes, name = 'test')
]