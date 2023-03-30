from django.forms import ModelForm
from .models import Akun, Angsuran


class AkunForm(ModelForm):
    model = Akun
    fields = '__all__'

class AngsuranForm(ModelForm):
    model = Angsuran
    fields = '__all__'