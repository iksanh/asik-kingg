from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from django.views.generic.edit import FormView
from django.contrib.auth.mixins import PermissionRequiredMixin
from .models import Member
from modul.pekerjaan.models import Pekerjaan
from modul.settings.models import Departement
from .forms import MemberForm, UploadCSVMember
from modul.crud_params import CrudParams
import csv
from datetime import datetime



# Create your views here.

#create parameter
member_param=CrudParams('member')

class MemberView(PermissionRequiredMixin, ListView, FormView):
    permission_required = ''
    model = Member
    template_name = 'member/list_member.html'
    context_object_name = 'data'
    
    

    #for upload data csv 
    form_class = UploadCSVMember
    success_url = reverse_lazy('list-member')

    extra_context = member_param.parameters(data_master=True, member=True)

    def form_valid(self, form):
        csv_file = form.cleaned_data['csv_file']
        decoded_file = csv_file.read().decode('utf-8').splitlines()
        reader = csv.DictReader(decoded_file)
        for row in reader:
            aktif = True if row['aktif'] == 'Y' else False
            pekerjaan = Pekerjaan.objects.get(nama=row['pekerjaan'])
            departement = Departement.objects.get(id=1)
            tanggal_lahir = datetime.strptime(row['tanggal_lahir'], "%m/%d/%Y")
            
            print(departement)
            Member.objects.create(
                nama=row['nama'],
                identitas=row['nik'],
                jenis_kelamin=row['jk'],
                tempat_lahir=row['tempat_lahir'],
                tanggal_lahir = tanggal_lahir,
                status= row['status'],
                agama= row['agama'],
                departement= departement,
                pekerjaan= pekerjaan,
                alamat= row['alamat'],
                kota= row['kota'],
                nomor_telpon= row['nomor_telepon'],
                aktif= aktif,
                # status= row['status']
                
            )
        return super().form_valid(form)




class MemberCreate(PermissionRequiredMixin, CreateView):
    permission_required = ''

    # model = Member
    form_class = MemberForm
    template_name = 'member/create_member.html'
    
    extra_context = member_param.parameters(data_master=True, member=True, action='Buat Data')
    success_url = reverse_lazy('list-member')


class MemberUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = ''
    model = Member
    template_name = 'member/create_member.html'
    fields = '__all__'
    extra_context = member_param.parameters(data_master=True, member=True, action='Edit Data')
    success_url = reverse_lazy('list-member')



def activate_member(request, id):
    member_id = get_object_or_404(Member, id=id)
    member_id.delete()
    return redirect('list-member')
    



