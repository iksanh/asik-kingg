from django.contrib.auth.views import LoginView
from django.contrib.auth.models import Group, Permission, PermissionManager, User
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.views.generic.edit import FormView, UpdateView
from .forms import RegisterUserForm, UpdateUserGroupForm
from django.contrib.auth import login
from django.views.generic import ListView, CreateView, DetailView, DeleteView
from django.urls import reverse_lazy
from django.contrib import  messages
from modul.crud_params import CrudParams
from modul.member.models import Member
from django.http import HttpResponse
# Create your views here.

modul = CrudParams('users')
modul_group = 'group'



class MyLoginView(LoginView):
    redirect_authenticated_user = True
    success_url = reverse_lazy('dashboard')

    def get_success_url(self):
        #get param next in url
        next_url= self.request.GET.get('next')
        return next_url if next_url else reverse_lazy('dashboard')


    def form_invalid(self, form):
        messages.error(self.request, "Username atau Password salah")
        return self.render_to_response(self.get_context_data(form=form))
    def form_valid(self, form):
        # Check the POST request fields
        #username = form.cleaned_data.get('username')
        # email = form.cleaned_data.get('email')
        #password = form.cleaned_data.get('password')
        #print(username, password)

        # Do something with the form data

        return super().form_valid(form)


class MyUserView(ListView):
    model = User
    template_name = 'users/user/list_user.html'
    context_object_name = 'data'
    extra_context = modul.parameters(users=True, data_master=True)



class MyUserRegistrationView(PermissionRequiredMixin, FormView): #PermissionRequiredMixin,
    #untuk hak akses
    permission_required = 'user.add_user'
    template_name = 'users/user/registration.html'
    form_class = RegisterUserForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('users')
    extra_context = modul.params

    def form_valid(self, form):
        user = form.save()
        if user:
            login(self.request, user)

        return super(MyUserRegistrationView, self).form_valid(form)

class MyUserUpdateView(UpdateView):
    model = User
    # form_class = RegisterUserForm

    template_name = 'users/user/registration.html'
    extra_context = modul.parameters(users=True, data_master=True, action='Update')

    def get_form_class(self):
        return RegisterUserForm
    def get_success_url(self):
        return reverse_lazy('users')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['groups'] = self.object.groups.all()
        return context

    def form_valid(self, form):
        return super(MyUserUpdateView, self).form_valid(form)

class MyUserUpdateGroup(MyUserUpdateView):
    def get_form_class(self):
        return UpdateUserGroupForm


def create_member_user(request, id):
    member = Member.objects.get(id=id)
    user = User.objects.create_user(username=member.identitas, password=member.identitas)
    user.save()

    member.user = user
    member.save()
    # Member(user=user, instance=member).save()
    # print(member.identitas)
    return redirect('list-member')
    # return HttpResponse(f"<h1>{member.identitas}</h1>")




def inactive_user(request, id):

    user = User.objects.filter(id = id)
    # print(User.objects.get(user))
    if request.method == 'GET':
        print(User.objects.get(id = id).is_active)
        user.update(is_active = False) if User.objects.get(id = id).is_active else user.update(is_active = True)

        return redirect('users')


class MyPermisionView(ListView):
    model = Permission
    template_name = 'users/permission/list_permission.html'
    context_object_name = 'data'


class MyGroupPermissionView(ListView):
    model = PermissionManager
    template_name = 'users/'