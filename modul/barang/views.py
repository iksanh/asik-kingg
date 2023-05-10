from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from .models import Barang
from django.views.generic import ListView, CreateView, UpdateView
from modul.crud_params import CrudParams

modul = CrudParams('barang')
# Create your views here.

class BarangView(ListView):
    model = Barang
    fields = '__all__'
    context_object_name = 'data'
    extra_context = modul.parameters(barang=True, data_master=True, action='Lihat Barang')

class BarangCreate(CreateView):
    model = Barang
    fields = '__all__'
    extra_context = modul.parameters(barang=True, data_master=True, action='Buat Barang')
    success_url = reverse_lazy('list-barang')

class BarangUpdate(UpdateView):
    model = Barang
    fields = '__all__'
    extra_context = modul.parameters(barang=True, data_master=True, action='Update Barang')
    success_url = reverse_lazy('list-barang')


def delete_barang(request, id):
    barang = get_object_or_404(Barang, id=id)
    barang.delete()
    return redirect('list-barang')



