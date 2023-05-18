from django import forms
from modul.simpanan.models import Simpanan, TransaksiSetoranSimpanan

class SimpananForm(forms.ModelForm):

    class Meta:
        model = Simpanan
        fields = '__all__'

class TransaksiSetoranForm(forms.ModelForm):

    class  Meta:
        model = TransaksiSetoranSimpanan
        fields = ('tanggal_transaksi','penyetor', 'nomor_identitas', 'alamat', 'jenis_transaksi', 'jumlah', 'keterangan','kas', 'anggota')
        widgets = {
            'tanggal_transaksi': forms.DateTimeInput(format=('%Y-%m-%dT%H:%M'), attrs={'type': 'datetime-local'})
        }