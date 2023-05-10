from django.urls import path, include 
from .views import MemberCreate, MemberUpdate, MemberView, activate_member

urlpatterns = [
  path('', MemberView.as_view(), name='list-member' ),
  path('create/', MemberCreate.as_view(), name='create-member' ),
  path('edit/<int:pk>', MemberUpdate.as_view(), name='edit-member' ),
  path('delete/<int:id>', activate_member, name='delete-member' )
]