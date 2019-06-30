from django import forms
from .models import AmishRegistrations, FeedBackFromAndroid


class Amish_Form(forms.ModelForm):

    class Meta:
        model = AmishRegistrations
        fields = ['name', 'college', 'city', 'mail', 'contact']


class Feed_form(forms.ModelForm):

    class Meta:
        model = FeedBackFromAndroid
        fields = ['name', 'mail', 'contact', 'msg']
