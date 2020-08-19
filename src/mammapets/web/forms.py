from django.forms import ModelForm
from django import forms
from .models import Contract


class ContractForm(ModelForm):
    class Meta:
        model = Contract
        fields = ['start_date', 'end_date', 'pet', 'mamma_pet', 'price', 'client']
        start_date = forms.DateField(
            widget=forms.DateInput(format='%m/%d/%Y', attrs={'class': 'datepicker'}),
            input_formats=('%m/%d/%Y',)
        )
        end_date = forms.DateField(
            widget=forms.DateInput(format='%m/%d/%Y', attrs={'class': 'datepicker'}),
            input_formats=('%m/%d/%Y',)
        )