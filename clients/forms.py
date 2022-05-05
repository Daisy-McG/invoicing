from django import forms
from .models import Client


class ClientForm (forms.ModelForm):
    """ Form to create and edit clients """
    class Meta:
        model = Client
        fields = [
            'client', 'address_line_one', 'address_line_two',
            'town', 'county', 'country', 'paid_to_date', 'balance',
            'email'
            ]
