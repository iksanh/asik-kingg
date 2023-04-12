from django.forms import ModelForm
from django import  forms
from modul.pinjaman.models import Pinjaman
from modul.simpanan.models import Simpanan

class PinjamanForm(ModelForm):

    class Meta:
        model = Pinjaman
        fields = '__all__'
