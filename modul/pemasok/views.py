from django.shortcuts import render, get_object_or_404, redirect
from .models import Pemasok
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from modul.crud_params import CrudParams

modul = CrudParams('pemasok')

#List View Pemaso 

class PemasokView(ListView):
    model = Pemasok
    context_object_name = 'data'
    extra_context = modul.parameters(data_master=True, pemasok=True, action='Lihat Data')

class PemasokCreate(CreateView):
    model = Pemasok
    fields = '__all__'
    extra_context = modul.parameters(data_master=True, pemasok=True, action='Buat Data')
    success_url = reverse_lazy('list-pemasok') 

class PemasokUpdate(UpdateView):
    model = Pemasok
    fields = '__all__'
    extra_context = modul.parameters(data_master=True, pemasok=True, action='Update Data')
    success_url = reverse_lazy('list-pemasok')

def delete_pemasok(request, pk):
    pemasok  = get_object_or_404(Pemasok, id=pk)
    pemasok.delete()
    return redirect('list-pemasok')




