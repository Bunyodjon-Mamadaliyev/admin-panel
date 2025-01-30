from django import forms
from .models import Order


class OrderForm(forms.Form):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('processing', 'Processing'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
    ]

    status = forms.ChoiceField(
        choices=STATUS_CHOICES,
        widget=forms.Select(attrs={
            'class': 'w-full px-3 py-2 text-gray-700 border rounded-lg focus:outline-none'
        })
    )
    customer_name = forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={
            'class': 'w-full px-3 py-2 text-gray-700 border rounded-lg focus:outline-none',
            'placeholder': 'Customer Name'
        })
    )
    customer_email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'w-full px-3 py-2 text-gray-700 border rounded-lg focus:outline-none',
            'placeholder': 'Customer Email'
        })
    )
    shipping_address = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'w-full px-3 py-2 text-gray-700 border rounded-lg focus:outline-none',
            'placeholder': 'Shipping Address',
            'rows': 3
        })
    )
    total_amount = forms.DecimalField(
        max_digits=10,
        decimal_places=2,
        widget=forms.NumberInput(attrs={
            'class': 'w-full px-3 py-2 text-gray-700 border rounded-lg focus:outline-none',
            'placeholder': 'Total Amount'
        })
    )
