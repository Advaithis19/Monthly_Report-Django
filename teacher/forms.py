from django import forms
from django.db.models import fields
from django.forms import widgets
from django.forms.widgets import PasswordInput, Select, TextInput, NumberInput, Textarea
from django.core.exceptions import ValidationError
from django.http import request
from api.models import *

class GrantForm(forms.ModelForm):
    """def __init__(self, *args, **kwargs):
        user = kwargs.pop('user','')
        super(GrantForm, self).__init__(*args, **kwargs)
        self.fields['PI']=forms.ModelChoiceField(queryset=Profile.objects.all())
        self.fields['CO_PI']=forms.ModelChoiceField(queryset=Profile.objects.all())"""

    class Meta:
        model = Grants
        exclude = ['date_added']

        widgets = {
            'title': TextInput(attrs={
                'style': 'width: 100%;',
                'placeholder': 'Title'
                }),
            'agency' : TextInput(attrs={
                'style': 'width: 100%',
                'placeholder': 'Agency',
            }),
            'sanc_amt': NumberInput(attrs={
                'style': 'width: 100%;',
                'placeholder': 'Sanction Amount',
            }),
            'year': NumberInput(attrs={
                'style': 'width: 100%;',
                'placeholder': 'Year',
            }),
            'remarks': Textarea(attrs={
                'style': 'width: 100%;',
                'placeholder': 'Remarks',
                'rows' : 5
            }),
            'PI': Select(attrs={
                'style': 'width: 100%;',
                'placeholder': 'PI',
            }),
            'CO_PI': Select(attrs={
                'style': 'width: 100%;',
                'placeholder': 'Co PI',
            }),
        }