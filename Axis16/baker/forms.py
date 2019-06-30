from django import forms
from main.models import BakerRegistration


class LoginForm(forms.ModelForm):

    class Meta:
        model = BakerRegistration
        fields = ['fname', 'fmail', 'idnum']
