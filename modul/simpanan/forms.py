from django.forms import ModelForm
from modul.simpanan.models import Simpanan

class SimpananForm(ModelForm):

    class Meta:
        model = Simpanan
        fields = '__all__'
