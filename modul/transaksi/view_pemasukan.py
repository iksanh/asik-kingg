# view untuk transaksi pemasukan 
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from .models import TransaksiKas
from .forms import PemasukanKasForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView
from modul.crud_params import CrudParams
from .views import OpsiAkun, DebitKredit
from django.contrib.auth.models import User

modul =  CrudParams('pemasukan_kas')

class PemasukanKasView(ListView):
    model = TransaksiKas
    fields = '__all__'
    context_object_name = 'data'
    extra_context = modul.parameters(transaksi=True, pemasukan_kas= True, action='Lihat Pemasukan Kas')
    queryset = TransaksiKas.objects.filter(akun=OpsiAkun.PEMASUKAN.value)

class PemasukanKasCreate(CreateView):
    form_class =  PemasukanKasForm
    extra_context = modul.parameters(transaksi=True, pemasukan_kas= True, action='Buat Pemasukan Kas')
    success_url = reverse_lazy('list-pemasukan_kas')

    def form_valid(self, form):
        akun = OpsiAkun.PEMASUKAN
        form.instance.akun = akun.value
        form.instance.user = User.objects.get(username=self.request.user)
        form.instance.debit_kredit = DebitKredit.DEBIT
        return super().form_valid(form)

class PemasukanKasUpdate(UpdateView):
    form_class = PemasukanKasForm
    model = TransaksiKas
    extra_context = modul.parameters(transaksi=True, pemasukan_kas= True, action='Edit Pemasukan Kas')
    success_url = reverse_lazy('list-pemasukan_kas')

    def form_valid(self, form):
        akun = OpsiAkun.PEMASUKAN
        form.instance.akun = akun.value
        form.instance.user = User.objects.get(username=self.request.user)
        form.instance.debit_kredit = DebitKredit.DEBIT
        return super().form_valid(form)


def delete_pemasukan(request, id):
    pemasukan_kas = get_object_or_404(TransaksiKas, id=id)
    pemasukan_kas.delete()
    return redirect('list-pemasukan_kas')