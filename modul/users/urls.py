from django.urls import  path
from .views import MyLoginView,  MyPermisionView,  MyUserView, MyUserRegistrationView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', MyLoginView.as_view(template_name = "users/login.html"), name= 'login'),
    path('logout/', LogoutView.as_view(next_page='login'), name= 'logout'),
    path('users/', MyUserView.as_view(), name= 'users'),
    path('users/create', MyUserRegistrationView.as_view(), name = 'create-users'),

    path('user/permission', MyPermisionView.as_view(), name= 'user-permission' )
]