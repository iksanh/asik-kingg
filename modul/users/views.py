from django.contrib.auth.views import LoginView
from django.contrib.auth.models import Group, Permission, PermissionManager, User
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.forms import UserCreationForm

from django.views.generic.edit import FormView, UpdateView
from .forms import RegisterUserForm
from django.contrib.auth import login

from django.views.generic import ListView, CreateView, DetailView, DeleteView
from django.urls import reverse_lazy
from django.contrib import  messages
from django.shortcuts import render

# Create your views here.
modul_group = 'group'
modul_user = 'users'


class MyLoginView(LoginView):
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('dashboard')

    def form_invalid(self, form):
        messages.error(self.request, "Username atau Password salah")
        return self.render_to_response(self.get_context_data(form=form))


class MyUserView(ListView):
    model = User
    template_name = 'users/user/list_user.html'
    context_object_name = 'data'
    extra_context = {
        'links': {
            'list': modul_user,
            'edit': 'edit-' + modul_user,
            'delete': 'delete-' + modul_user,
            'create': 'create-' + modul_user
        }
    }

class MyUserRegistrationView(PermissionRequiredMixin, FormView):
    #untuk hak akses
    permission_required = 'user.add_user'
    template_name = 'users/user/registration.html'
    form_class = RegisterUserForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('users')
    extra_context = {
        'action': 'Buat',
        'modul': modul_user,
        'links': {
            'list': modul_user,
            'edit': 'edit-' + modul_user,
            'delete': 'delete-' + modul_user,
            'create': 'create-' + modul_user
        }
    }

    def form_valid(self, form):
        user = form.save()
        if user:
            login(self.request, user)

        return super(MyUserRegistrationView, self).form_valid(form)



class MyPermisionView(ListView):
    model = Permission
    template_name = 'users/permission/list_permission.html'
    context_object_name = 'data'


class MyGroupPermissionView(ListView):
    model = PermissionManager
    template_name = 'users/'