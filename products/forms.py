from django import forms
from .models import Product
from categories.models import Category


class ProductForm(forms.Form):
    class Meta:
        model = Product
    name = forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={
            'class': 'w-full px-3 py-2 text-gray-700 border rounded-lg focus:outline-none',
            'placeholder': 'Product Name'
        })
    )
    description = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'w-full px-3 py-2 text-gray-700 border rounded-lg focus:outline-none',
            'placeholder': 'Product Description',
            'rows': 4
        })
    )
    price = forms.DecimalField(
        max_digits=10,
        decimal_places=2,
        widget=forms.NumberInput(attrs={
            'class': 'w-full px-3 py-2 text-gray-700 border rounded-lg focus:outline-none',
            'placeholder': 'Price'
        })
    )
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        widget=forms.Select(attrs={
            'class': 'w-full px-3 py-2 text-gray-700 border rounded-lg focus:outline-none'
        })
    )
    image = forms.ImageField(
        widget=forms.FileInput(attrs={
            'class': 'w-full px-3 py-2 text-gray-700 border rounded-lg focus:outline-none'
        })
    )

    def clean_price(self):
        price = self.cleaned_data['price']
        if price <= 0:
            raise forms.ValidationError("Price must be greater than zero.")
        return price
