from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group, Permission

class RegisterUserForm(UserCreationForm):
    qs_group = Group.objects.all()
    group = forms.ModelMultipleChoiceField(queryset=qs_group, widget=forms.CheckboxSelectMultiple)
    email = forms.EmailField(max_length=255)

    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)
        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

    def save(self, commit=True):
        #buat instance
        instance = super().save(commit=commit)
        instance.groups.clear()

        for option_group in self.cleaned_data['group']:
            instance.groups.add(option_group)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'group')





