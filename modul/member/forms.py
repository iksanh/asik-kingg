from django import forms
from .models import Member
from modul.crud_params import Opsi
from modul.pekerjaan.models import Pekerjaan
from django.forms.widgets import RadioSelect
import csv

class CustomRadioSelect(RadioSelect):
    def create_option(self, name, value, label, selected, index, subindex=None, attrs=None):
        option = super().create_option(name, value, label, selected, index, subindex=subindex, attrs=attrs)
        # Remove the dash and underscores from the label and radio button
        option['label'] = label.replace('_', ' ')
        option['label'] = option['label'].replace('-', ' ')
        option['label'] = option['label'].capitalize()
        option['value'] = value.replace('_', '-')
        return option

class MemberForm(forms.ModelForm):
    # q_pekerjaan = Pekerjaan.objects.all()
    
    # jenis_kelamin=forms.ChoiceField(choices=Opsi.JENIS_KELAMIN, widget=CustomRadioSelect)
    # pekerjaan = forms.ModelChoiceField(queryset=q_pekerjaan)
    alamat = forms.CharField(widget=forms.Textarea(attrs={"rows":"2"}))
    class Meta:
        model = Member
        fields = '__all__'
    
class UploadCSVMember(forms.Form):
    csv_file = forms.FileField(label='Pilih File')
