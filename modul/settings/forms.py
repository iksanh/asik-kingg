from django import forms
from .models import (
    Settings,
    Departement,
    FileRat
)

class SettingsForm(forms.ModelForm):
         
    class Meta:
        model = Settings
        fields = '__all__'

class DepartementForm(forms.ModelForm):
    pass

class FileRatForm(forms.ModelForm):
    pass