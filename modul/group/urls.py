from django.urls import path
from .views import MyGroupView, MyGroupCreateView, MyGroupUpdateView, delete_group

urlpatterns = [
    path('list', MyGroupView.as_view(), name='group'),
    path('create', MyGroupCreateView.as_view(), name='create-group'),
    path('<int:pk>/edit/', MyGroupUpdateView.as_view(), name='edit-group'),
    path('<int:id>/delete/', delete_group, name= 'delete-group')
]
