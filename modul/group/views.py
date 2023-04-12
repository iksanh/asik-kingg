from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, CreateView, FormView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.models import Group
from .forms import RegisterGropForm

# Create your views here.
modul_group = 'group'
class MyGroupView(PermissionRequiredMixin,ListView):
    #add permission
    permission_required = 'group.add_group'
    model = Group
    template_name = 'users/group/list_group.html'
    context_object_name = 'data'

    extra_context = {
        'links': {
            'list': modul_group,
            'edit': 'edit-' + modul_group,
            'delete': 'delete-' + modul_group,
            'create': 'create-' + modul_group
        }
    }


class MyGroupCreateView(FormView):
    model = Group
    template_name ='users/group/create_group.html'
    permission_required = 'group.view_group'
    form_class = RegisterGropForm
    context_object_name = 'form'
    success_url = reverse_lazy('group')
    extra_context = {
        'modul' : modul_group,
        'links': {
            'list': modul_group,
            'edit': 'edit-' + modul_group,
            'delete': 'delete-' + modul_group,
            'create': 'create-' + modul_group
        }
    }
    def form_valid(self, form):
        group = form.save()

        form.instance.user = self.request.user
        return super(MyGroupCreateView,self).form_valid(form)

class MyGroupUpdateView(UpdateView):
    model = Group
    form_class = RegisterGropForm
    template_name ='users/group/create_group.html'

    success_url = reverse_lazy('group')

    extra_context = {
        'modul': modul_group,
        'links': {
            'list': modul_group,
            'edit': 'edit-' + modul_group,
            'delete': 'delete-' + modul_group,
            'create': 'create-' + modul_group
        }
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['permission'] = self.object.permissions.all()
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.permissions.set(form.cleaned_data['permissions'])
        self.object.save()
        return super().form_valid(form)


