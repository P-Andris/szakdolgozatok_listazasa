from django import forms
from django.forms import ModelForm, ValidationError
from .models import Szakdoga

class SzakdogaForm(ModelForm):
    class Meta:
        model = Szakdoga
        # fields = ['szakdoga_neve', 'githublink', 'oldallink', 'tagokneve']
        fields = '__all__'