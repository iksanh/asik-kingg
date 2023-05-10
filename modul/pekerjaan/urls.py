from django.urls import path
from .views import PekerjaanView, PekerjaanUpdate, PekerjaanCreate, pekerjaan_delete

## url for pekerjaan

urlpatterns = [
    path('', PekerjaanView.as_view(), name='list-pekerjaan'),
    path('create/', PekerjaanCreate.as_view(), name='create-pekerjaan'),
    path('edit/<int:pk>', PekerjaanUpdate.as_view(), name='edit-pekerjaan'),
    path('delete/<int:id>', pekerjaan_delete, name='delete-pekerjaan')
]
    