from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from .models import Pekerjaan
from modul.crud_params import CrudParams
from django.views.generic import ListView, CreateView, UpdateView


#create parameters 
pekerjaan_params = CrudParams('pekerjaan')
# Create your views here.
class PekerjaanView(ListView):
    model = Pekerjaan
    template_name = 'pekerjaan/list_pekerjaan.html'
    context_object_name = 'data'
    extra_context = pekerjaan_params.parameters(data_master=True, pekerjaan=True)

class PekerjaanCreate(CreateView):
    model = Pekerjaan
    template_name = 'pekerjaan/create_pekerjaan.html'
    fields = '__all__'
    extra_context = pekerjaan_params.parameters(data_master=True, pekerjaan=True, action='Buat Data')
    success_url = reverse_lazy('list-pekerjaan')  

class PekerjaanUpdate(UpdateView):
    model = Pekerjaan
    fields = '__all__'
    template_name = 'pekerjaan/create_pekerjaan.html'
    extra_context = pekerjaan_params.parameters(data_master=True, pekerjaan=True, action='Edit Data')
    success_url = reverse_lazy('list-pekerjaan') 

def pekerjaan_delete(request, id):
    angsuran = get_object_or_404(Pekerjaan, id= id)
    angsuran.delete()
    return redirect('list-angsuran')