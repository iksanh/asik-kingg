from django.urls import  path
from .views import MyLoginView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', MyLoginView.as_view(template_name = "users/login.html"), name= 'login'),
    path('logout/', LogoutView.as_view(next_page='login'), name= 'logout')
]