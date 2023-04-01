from django.forms import ModelForm
from .models import Akun, Angsuran


class AkunForm(ModelForm):
    class Meta:
        model = Akun
        fields = '__all__'

class AngsuranForm(ModelForm):
    class Meta:
        model = Angsuran
        fields = '__all__'