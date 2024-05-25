# forms.py
from django import forms
from .models import Supply

class SupplyForm(forms.ModelForm):
    class Meta:
        model = Supply
        fields = ['item_name', 'quantity', 'supplier', 'supplyer_name']
