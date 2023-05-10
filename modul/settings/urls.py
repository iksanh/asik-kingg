from django.urls import path
from .views import  (SettingsView,
                      CreateSettings, 
                      DepartementView, DepartementCreate, DepartementUpdate, departement_delete) 


urlpatterns = [
  path('', SettingsView.as_view(), name='list-settings'),
  path('create', CreateSettings.as_view(), name='create-settings'),

  path('departement/', DepartementView.as_view(), name='list-departement'),
  path('create/departement', DepartementCreate.as_view(), name='create-departement'),
  path('edit/departement/<int:pk>', DepartementUpdate.as_view(), name='edit-departement'),
  path('delete/departement/<int:id>', departement_delete, name='delete-departement'),
]