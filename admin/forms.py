from django import forms
from django.forms.widgets import Select

class DateForm(forms.Form):
    MONTH_CHOICES = [
        (1,"January"),
        (2,"February"),
        (3,"March"),
        (4,"April"),
        (5,"May"),
        (6,"June"),
        (7,"July"),
        (8,"August"),
        (9,"September"),
        (10,"October"),
        (11,"November"),
        (12,"December"),
    ]
    month = forms.ChoiceField(
        choices=MONTH_CHOICES,
        widget=forms.Select(attrs={
            'style': 'width:100%'
        })
    )
    year = forms.IntegerField(widget=forms.NumberInput(attrs={'maxlength': 4, 'required': True, 'value': 2021, 'style' : 'width:100%;'}))