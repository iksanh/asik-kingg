# view untuk transaksi pengeluaran
from typing import Any
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from .models import TransaksiKas
from .forms import PengeluaranKasForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView
from modul.crud_params import CrudParams
from .views import OpsiAkun, DebitKredit
from django.contrib.auth.models import User
from modul.crud_params import CrudParams

modul = CrudParams('pengeluaran_kas')

class PengeluaranView(ListView):
    model = TransaksiKas
    context_object_name = 'data'
    extra_context = modul.parameters(transaksi=True, pengeluaran_kas=True, action='Lihat Pengeluaran Kas')
    
    def get_queryset(self):
        query_set = super().get_queryset()
        return query_set.filter(akun=OpsiAkun.PENGELUARAN.value)

class PengeluaranKasCreate(CreateView):
    form_class = PengeluaranKasForm
    extra_context = modul.parameters(transaksi=True, pengeluaran_kas= True, action='Buat Pengeluaran Kas')
    success_url = reverse_lazy('list-pengeluaran_kas')

    def form_valid(self, form):
        akun  = OpsiAkun.PENGELUARAN
        form.instance.akun = akun.value
        form.instance.user = User.objects.get(username=self.request.user)
        form.instance.debit_kredit = DebitKredit.KREDIT.value
        return super().form_valid(form)
    
class PengeluaranKasUpdate(UpdateView):
    
    form_class = PengeluaranKasForm
    model = TransaksiKas
    extra_context = modul.parameters(transaksi=True, pengeluaran_kas= True, action='Update Pengeluaran Kas')
    
    success_url = reverse_lazy('list-pengeluaran_kas')

    def form_valid(self, form):
        akun  = OpsiAkun.PENGELUARAN
        form.instance.akun = akun.value
        form.instance.user = User.objects.get(username=self.request.user)
        form.instance.debit_kredit = DebitKredit.KREDIT.value
        return super().form_valid(form)


def delete_pengeluaran(request, id):
    pengeluaran = get_object_or_404(TransaksiKas, id=id)
    pengeluaran.delete()
    return redirect('list-pengeluaran_kas')