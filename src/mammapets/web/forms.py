from django.forms import ModelForm
from django import forms

from .models import Contract


class ContractForm(ModelForm):
    class Meta:
        model = Contract
        fields = ['start_date', 'end_date', 'pet', 'mamma_pet', 'price', 'client']