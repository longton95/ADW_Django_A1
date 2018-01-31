from django import forms
from .models import Wallet

class walletForm (forms.ModelForm):

    name = forms.CharField (label = 'Wallet Name', widget = forms.TextInput (attrs = {'size' : 32}))
    bitcoin = forms.DecimalField (label = 'Bitcoin', widget = forms.NumberInput (attrs = {'size' : 64}))
    etherium = forms.DecimalField (label = 'Etherium', widget = forms.NumberInput (attrs = {'size' : 64}))
    litecoin = forms.DecimalField (label = 'Litecoin', widget = forms.NumberInput (attrs = {'size' : 64}))


    class Meta:
        model = Wallet
        fields = ('name', 'bitcoin', 'etherium', 'litecoin',)