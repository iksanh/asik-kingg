from django.shortcuts import render
from django.urls import reverse_lazy
from modul.crud_params import CrudParams

from django.views.generic import (
    ListView, CreateView
)
from django.contrib.auth.mixins import PermissionRequiredMixin
from .models import (
    Settings,
    Departement,
    FileRat
)

from .forms import (
    SettingsForm,
    DepartementForm,
    FileRatForm
)

parameter_settings = CrudParams('setting')
parameter_departement = CrudParams('departement')
paramater_file_rat = CrudParams('file_rat')


#View for settings 
class SettingsView(PermissionRequiredMixin,ListView):
    permission_required = ''
    model = Settings
    template_name = 'settings/list_settings.html' 
    context_object_name = 'data' 
    extra_context = parameter_settings.parameters(settings=True, identitas=True)

class CreateSettings(PermissionRequiredMixin, CreateView):
    permission_required = ''
    # form_class = SettingsForm
    model = Settings 
    data = Settings.objects.all()
    fields = ['opsi_key', 'opsi_val']
    template_name =  'settings/create_settings.html'
    
    extra_context = parameter_settings.parameters(settings=True, identitas=True, data=data)
    success_url = reverse_lazy('list-settings')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateSettings, self).form_valid(form)



# Create your views here. 
