from django import forms
from .models import Donate

class DonateForm(forms.ModelForm):
    class Meta:
        model = Donate
        fields = [
            "image",
            "shirt_qty",
            "pant_qty",
            "blanket_qty",
            "books_qty",
            "other_qty",
            "furniture_qty",
            "furniture_description",
        ]
