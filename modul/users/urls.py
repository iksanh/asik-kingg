from django.urls import  path
from .views import MyLoginView,  MyPermisionView,  MyUserView, MyUserRegistrationView, MyUserUpdateView, inactive_user
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', MyLoginView.as_view(template_name = "users/login.html"), name= 'login'),
    path('logout/', LogoutView.as_view(next_page='login'), name= 'logout'),
    path('list/', MyUserView.as_view(), name= 'users'),
    path('create', MyUserRegistrationView.as_view(), name='create-users'),
    path('<int:pk>/edit/', MyUserUpdateView.as_view(), name='edit-users'),
    path('<int:id>/status', inactive_user, name = 'inactive_user' ),
    # path('<int:id>/edit/', user_update, name='edit-users'),

    path('user/permission', MyPermisionView.as_view(), name='user-permission')
]