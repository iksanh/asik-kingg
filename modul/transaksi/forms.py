from django import forms
from .models import Akun, Angsuran, TransaksiKas, JurnalAkun
from modul.kas.models import Kas



class AkunForm(forms.ModelForm):
    class Meta:
        model = Akun
        fields = '__all__'

class AngsuranForm(forms.ModelForm):
    class Meta:
        model = Angsuran
        fields = '__all__'

class PemasukanKasForm(forms.ModelForm):
    jenis_transaksi = forms.ModelChoiceField(queryset=Akun.objects.filter(pemasukan='Y', aktif='Y'),
    label='Dari Akun')
    
    
    class Meta:
        model = TransaksiKas
        fields = ['tanggal_catat','jumlah', 'keterangan', 'jenis_transaksi', 'untuk_kas' ] 
        widgets = {
            'tanggal_catat': forms.DateTimeInput(format=('%Y-%m-%dT%H:%M'), attrs={'type': 'datetime-local'})
        }


class PengeluaranKasForm(forms.ModelForm):
    jenis_transaksi = forms.ModelChoiceField(queryset=Akun.objects.filter(pengeluaran='Y', aktif='Y',),
    label='Untuk Akun')
    
    
    class Meta:
        model = TransaksiKas
        fields = ['tanggal_catat','jumlah', 'keterangan', 'dari_kas', 'jenis_transaksi'] 
        widgets = {
            'tanggal_catat': forms.DateTimeInput(format=('%Y-%m-%dT%H:%M'), attrs={'type': 'datetime-local'})
            
        }

class TransferKasForm(forms.ModelForm):
    
    class Meta:
        model = TransaksiKas
        fields = ['tanggal_catat','jumlah', 'keterangan', 'dari_kas', 'untuk_kas'] 
        widgets = {
            'tanggal_catat': forms.DateTimeInput(format=('%Y-%m-%dT%H:%M'), attrs={'type': 'datetime-local'})
            
        }

class JurnalAkunForm(forms.ModelForm):
    
    class Meta:
        model = JurnalAkun
        fields = ['tanggal_transaksi','jumlah', 'dari_akun', 'untuk_akun', 'keterangan'] 
        widgets = {
            'tanggal_transaksi': forms.DateTimeInput(format=('%Y-%m-%dT%H:%M'), attrs={'type': 'datetime-local'})
            
        }