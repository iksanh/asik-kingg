# view untuk transaksi transfer
import io
from typing import Any
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from .models import TransaksiKas, Akun, JurnalAkun
from .forms import TransferKasForm, JurnalAkunForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView, View
from modul.crud_params import CrudParams
from modul import utils
from .views import OpsiAkun
from django.contrib.auth.models import User
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from docx import Document

from modul.crud_params import CrudParams

modul = CrudParams('transfer_kas')
modul_jurnal = CrudParams('jurnal_akun')

class TransferView(ListView):
   
    model = TransaksiKas
    context_object_name = 'data'
    extra_context = modul.parameters(transaksi=True, transfer_kas=True, action='Lihat Transfer Kas')
    
    def get_queryset(self):
        query_set = super().get_queryset()
        return query_set.filter(akun=OpsiAkun.TRANSFER.value)



class TransferKasCreate(CreateView):
    form_class = TransferKasForm
    extra_context = modul.parameters(transaksi=True, transfer_kas= True, action='Buat Transfer Kas')
    success_url = reverse_lazy('list-transfer_kas')

    def form_valid(self, form):
        akun  = OpsiAkun.TRANSFER
        form.instance.akun = akun.value
        form.instance.user = User.objects.get(username=self.request.user)
        form.instance.jenis_transaksi = Akun.objects.get(id=110)
        # form.instance.debit_kredit = DebitKredit.KREDIT.value
        return super().form_valid(form)
    
class TransferKasUpdate(UpdateView):
    
    form_class = TransferKasForm
    model = TransaksiKas
    extra_context = modul.parameters(transaksi=True, transfer_kas= True, action='Update Pengeluaran Kas')
    success_url = reverse_lazy('list-transfer_kas')

    def form_valid(self, form):
        akun  = OpsiAkun.TRANSFER
        form.instance.akun = akun.value
        form.instance.user = User.objects.get(username=self.request.user)
        # form.instance.debit_kredit = DebitKredit.KREDIT.value
        return super().form_valid(form)


class ReportTransferKas(View):
    
    def get(self, request , *args , **kwargs):

        id = self.request.GET.get('id')
        print(id)
        #ambil data dari database
        if id:
            transfer = TransaksiKas.objects.get(id=id)
            context ={
                'transfer': transfer
            }
            pdf = utils.render_to_pdf('transaksi/invoice.html', context)
            return HttpResponse(pdf, content_type='application/pdf')
        
       
        queryset = TransaksiKas.objects.filter(akun=OpsiAkun.TRANSFER.value)
        

        context = {
            'data':queryset
        }   
        # print(context['dat'])

        pdf_all = utils.render_to_pdf('transaksi/transfer_kas/report_transfer_kas.html', context) 
        return HttpResponse(pdf_all, content_type='application/pdf')
        # return render(request,'transaksi/transfer_kas/report_transfer_kas.html', context)
        
def delete_transfer(request, id):
    transfer = get_object_or_404(TransaksiKas, id=id)
    transfer.delete()
    return redirect('list-transfer_kas')


class TransferJurnalAkunView(ListView):
      model = JurnalAkun
      context_object_name = 'data'
      extra_context = modul_jurnal.parameters(transaksi=True, jurnal_akun=True, action='Lihat Jurnal Akun')

      
      
class TransferJurnalCreate(CreateView):
    form_class = JurnalAkunForm
    success_url = reverse_lazy('list-jurnal_akun')
    extra_context = modul_jurnal.parameters(transaksi=True, jurnal_akun=True, action='Tambah Jurnal Akun')


    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.user = User.objects.get(username=self.request.user)
        return super().form_valid(form)
        
class TransferJurnalUpdate(UpdateView):
    model = JurnalAkun
    form_class = JurnalAkunForm
    success_url = reverse_lazy('list-jurnal_akun')
    extra_context = modul_jurnal.parameters(transaksi=True, jurnal_akun=True, action='Edit Jurnal Akun')

def delete_jurnal_akun(request, id):
    transfer = get_object_or_404(TransaksiKas, id=id)
    transfer.delete()
    return redirect('list-jurnal_akun')

class ReportJurnalAkun(View):
    
    def get(self, request , *args , **kwargs):

        id = self.request.GET.get('id')
        print(id)
        #ambil data dari database
        if id:
            transfer = TransaksiKas.objects.get(id=id)
            context ={
                'transfer': transfer
            }
            pdf = utils.render_to_pdf('transaksi/invoice.html', context)
            return HttpResponse(pdf, content_type='application/pdf')
        
       
        queryset = JurnalAkun.objects.all()
        

        context = {
            'data':queryset
        }   
        # print(context['dat'])

        pdf_all = utils.render_to_pdf('transaksi/transfer_kas/report_transfer_kas.html', context) 
        return HttpResponse(pdf_all, content_type='application/pdf')
        # return render(request,'transaksi/transfer_kas/report_transfer_kas.html', context)
