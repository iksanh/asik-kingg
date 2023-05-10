from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView
from modul.crud_params import CrudParams
from .forms import AkunForm, AngsuranForm
from .models import Akun, Angsuran
from enum import Enum

# Create your views here.
akun_params = CrudParams('akun')
angsuran_params = CrudParams('angsuran')

class AkunView(ListView):
    model = Akun
    template_name = 'transaksi/akun/list_akun.html'
    context_object_name = 'data'
    extra_context = akun_params.parameters(data_master=True, akun=True)

def list_akun(request):
    template_list =  'transaksi/akun/list_akun.html'
    akun= Akun.objects.all()
    context = {'data': akun}
    return render(request, template_list, context )


def create_akun(request):
    template_create = 'transaksi/akun/create_akun.html'

    if request.method == 'GET':
        form = AkunForm()
        context = akun_params.parameters(form=form, data_master=True, akun=True, action='Buat Data') 
        return render(request, template_create, context)
    elif request.method == 'POST':
        form= AkunForm(request.POST)
        context = akun_params.parameters(form=form, data_master=True, akun=True, action='Buat Data') 
        if form.is_valid():
            form.save()
            return redirect('list-akun')
        else:
            return render(request, template_create, context)


def delete_akun(request, id):
    akun = get_object_or_404(Akun, id= id)
    akun.delete()
    return redirect('list-akun')

def edit_akun(request, id):
    template_create = 'transaksi/akun/create_akun.html'
    akun = get_object_or_404(Akun, id=id)

    context = akun_params.parameters(form=AkunForm(instance=akun), id=id, data_master=True, akun=True, action='Edit Data') 
    if request.method == 'GET':
        return render(request, template_create,  context)

    elif request.method == 'POST':
        form = AkunForm(request.POST, instance=akun)
        context = akun_params.parameters(form=form, data_master=True, akun=True, action='Edit Data')
        if form.is_valid():
            form.save()
            return redirect('list-akun')
        else:
            return render(request, template_create, context)




class AngsuranView(ListView):
    model = Angsuran
    template_name = 'transaksi/angsuran/list_angsuran.html'
    context_object_name = 'data'
    extra_context = angsuran_params.parameters(data_master=True, angsuran=True)

class AngsuranCreate(CreateView):
    model = Angsuran
    template_name = 'transaksi/angsuran/create_angsuran.html'
    fields = '__all__'
    extra_context = angsuran_params.parameters(data_master=True, angsuran=True, action='Buat Data')
    success_url = reverse_lazy('list-angsuran')  

class AngsuranUpdate(UpdateView):
    model = Angsuran
    fields = '__all__'
    template_name = 'transaksi/angsuran/create_angsuran.html'
    extra_context = angsuran_params.parameters(data_master=True, angsuran=True, action='Edit Data')
    success_url = reverse_lazy('list-angsuran') 

def angsuran_delete(request, id):
    angsuran = get_object_or_404(Angsuran, id= id)
    angsuran.delete()
    return redirect('list-angsuran')

class OpsiAkun(Enum):
    PEMASUKAN = 'Pemasukan'
    PENGELUARAN = 'Pengeluaran'
    TRANSFER = 'Transfer'

class DebitKredit(Enum):
    DEBIT = 'D'
    KREDIT = 'K'