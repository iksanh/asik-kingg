from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from modul.simpanan.views import (
    list_simpanan, create_simpanan, edit_simpanan, delete_simpanan,
    SetoranSimpananCreate, SetoranSimpananUpdate, SetoranSimpananView, delete_setoran_simpanan, tes,
    PenarikanSimpananCreate, PenarikanSimpananUpdate, PenarikanSimpananView, delete_penarikan_simpanan
 )


urlpatterns = [
    path('', list_simpanan, name='simpanan'),
    path('create/', create_simpanan, name = 'create-simpanan'),
    path('edit/<int:id>/', edit_simpanan, name = 'edit-simpanan'),
    path('delete/<int:id>/', delete_simpanan, name = 'delete-simpanan'),
    path('test', tes, name = 'test'),

    #url setor simpanan
    path('setor_simpanan/', SetoranSimpananView.as_view(template_name='simpanan/setoran_simpanan/list_simpanan.html'), name = 'list-setor_simpanan'),
    path('setor_simpanan/create/', SetoranSimpananCreate.as_view(template_name = 'simpanan/setoran_simpanan/create_simpanan.html'), name = 'create-setor_simpanan'),
    path('setor_simpanan/edit/<int:pk>/', SetoranSimpananUpdate.as_view(template_name= 'simpanan/setoran_simpanan/create_simpanan.html'), name = 'edit-setor_simpanan'),
    path('setor_simpanan/delete/<int:id>/', delete_setoran_simpanan, name = 'delete-setor_simpanan'),

    #url penarikan simpanan
    path('penarikan_simpanan/', PenarikanSimpananView.as_view(template_name='simpanan/penarikan/list_penarikan.html'), name = 'list-penarikan_simpanan'),
    path('penarikan_simpanan/create/', PenarikanSimpananCreate.as_view(template_name = 'simpanan/penarikan/create_penarikan.html'), name = 'create-penarikan_simpanan'),
    path('penarikan_simpanan/edit/<int:pk>/', PenarikanSimpananUpdate.as_view(template_name= 'simpanan/penarikan/create_penarikan.html'), name = 'edit-penarikan_simpanan'),
    path('penarikan_simpanan/delete/<int:id>/', delete_setoran_simpanan, name = 'delete-penarikan_simpanan'),
    
]