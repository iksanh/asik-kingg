from typing import Any
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.models import User
from django.views.generic import ListView, UpdateView, CreateView
from .forms import SimpananForm, Simpanan, TransaksiSetoranForm, TransaksiPenarikanForm
from .models import TransaksiSetoranSimpanan
from modul.member.models import Member
from modul.crud_params import CrudParams
from modul.transaksi.views import DebitKredit,SetoranPenarikan


simpanan_param = CrudParams('simpanan')
modul_sp = CrudParams('setor_simpanan')
modul_ps= CrudParams('penarikan_simpanan')

# Create your views here.

# @permission_required('view_akun')
def list_simpanan(request):
    simpanan_data = Simpanan.objects.all()
    context = simpanan_param.parameter(data=simpanan_data, simpanan=True, data_master=True)

    return render(request, 'simpanan/list_simpanan.html', context)

def create_simpanan(request):
    tempalate_file = 'simpanan/create_simpanan.html'
    if request.method == 'GET':
        context = simpanan_param.parameter(form=SimpananForm(), simpanan=True, data_master=True)
        print(context)
        return render(request, tempalate_file, context)
    elif request.method == 'POST':
        simpanan_form = SimpananForm(request.POST)
        print(request.POST)
        if simpanan_form.is_valid():
            simpanan_form.save()
            return redirect('simpanan')
        else:
            return render(request, tempalate_file, simpanan_param.parameter(form=simpanan_form, simpanan=True, data_master=True))

def edit_simpanan(request, id):
    simpanan = get_object_or_404(Simpanan, id = id)
    if request.method == 'GET':
        context = simpanan_param.parameter(form=SimpananForm(instance=simpanan), id=id, simpanan=True, data_master=True)
        return render(request, 'simpanan/create_simpanan.html', context)
    elif request.method =='POST':
        simpanan_form = SimpananForm(request.POST, instance=simpanan)
        if simpanan_form.is_valid():
            simpanan_form.save()
            return redirect('simpanan')

        else:
            return render(request, 'simpanan/create_simpanan.html', simpanan_param.parameter(form=simpanan_form, simpanan=True, data_master=True))

def delete_simpanan(request, id):
    simpanan = get_object_or_404(Simpanan, id=id)
    simpanan.delete()
    return redirect('simpanan')

def tes(request):
    return render(request, 'simpanan/login.html', context={'data': 'data'})


class SetoranSimpananView(ListView):
    model = TransaksiSetoranSimpanan
    context_object_name = 'data'
    extra_context = modul_sp.parameters(data_simpanan=True, setor_simpanan=True, action='Lihat Data Setor Simpanan')
    def get_queryset(self) -> QuerySet[Any]:
        return TransaksiSetoranSimpanan.objects.filter(akun= SetoranPenarikan.SETORAN.value)

class SetoranSimpananCreate(CreateView):
    # model = TransaksiSetoranSimpanan
    # fields = '__all__'
    form_class = TransaksiSetoranForm
    member = Member.objects.values('id', 'nama')
    extra_context = modul_sp.parameters(data_simpanan=True, setor_simpanan=True, action='Tambah Data Setor Simpanan', data_member=member)
    success_url = reverse_lazy('list-setor_simpanan')
    
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.user = User.objects.get(username=self.request.user)
        form.instance.dk = DebitKredit.DEBIT.value
        form.instance.akun = SetoranPenarikan.SETORAN.value
        
        return super().form_valid(form)

class SetoranSimpananUpdate(UpdateView):
     model = TransaksiSetoranSimpanan
     form_class = TransaksiSetoranForm
     extra_context = modul_sp.parameters(data_simpanan=True, setor_simpanan=True, action='Tambah Data Setor Simpanan')
     success_url = reverse_lazy('list-setor_simpanan')
    
     def form_valid(self, form: BaseModelForm) -> HttpResponse:
        
        form.instance.user = User.objects.get(username=self.request.user)
        form.instance.dk = DebitKredit.DEBIT.value
        form.instance.akun = SetoranPenarikan.SETORAN.value
        return super().form_valid(form)

def delete_setoran_simpanan(req, id):
    setor_simpan = get_object_or_404(TransaksiSetoranSimpanan, id=id)
    setor_simpan.delete()

    return redirect('list-setor_simpanan')

class PenarikanSimpananView(ListView):
    model = TransaksiSetoranSimpanan
    extra_context = modul_ps.parameters(data_simpanan=True, penarikan_simpanan=True, action='Data Penarikan Simpanan')
    context_object_name = 'data'
    success_url = reverse_lazy('list-penarikan_simpanan')

    def get_queryset(self) -> QuerySet[Any]:
        return TransaksiSetoranSimpanan.objects.filter(akun= SetoranPenarikan.PENARIKAN.value)


class PenarikanSimpananCreate(CreateView):
    
    form_class = TransaksiPenarikanForm
    member = Member.objects.values('id', 'nama')
    extra_context = modul_ps.parameters(data_simpanan=True, penarikan_simpanan=True, action='Tambah Data Setor Simpanan', data_member=member)
    success_url = reverse_lazy('list-penarikan_simpanan')
    
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.user = User.objects.get(username=self.request.user)
        form.instance.dk = DebitKredit.KREDIT.value
        form.instance.akun = SetoranPenarikan.PENARIKAN.value
        print(self.request.POST.get('anggota'))
        
        return super().form_valid(form)

class PenarikanSimpananUpdate(UpdateView):
    model = TransaksiSetoranSimpanan
    form_class = TransaksiPenarikanForm
    member = Member.objects.values('id', 'nama')
    extra_context = modul_ps.parameters(data_simpanan=True, penarikan_simpanan=True, action='Tambah Data Setor Simpanan', data_member=member)
    success_url = reverse_lazy('list-penarikan_simpanan')
    
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.user = User.objects.get(username=self.request.user)
        form.instance.dk = DebitKredit.KREDIT.value
        form.instance.akun = SetoranPenarikan.PENARIKAN.value
        
        return super().form_valid(form)
    
def delete_penarikan_simpanan(req, id):
    penarikan_simpanan = get_object_or_404(TransaksiSetoranSimpanan, id=id)
    penarikan_simpanan.delete()
    return redirect('list-penarikan_simpanan')