from django.forms import ModelForm
from .models import Kas

class KasForm(ModelForm):

    class Meta:
        model =Kas
        fields ='__all__'