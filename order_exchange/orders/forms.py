from django import forms

from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        exclude = ('customer', 'executor', 'created_at')
