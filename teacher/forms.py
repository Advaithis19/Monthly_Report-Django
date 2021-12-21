from django import forms
from django.db.models import fields
from django.forms import widgets
from django.forms.widgets import PasswordInput, Select, SelectDateWidget, SelectMultiple, TextInput, NumberInput, Textarea
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


class EventForm(forms.ModelForm):
    """def __init__(self, *args, **kwargs):
        user = kwargs.pop('user','')
        super(GrantForm, self).__init__(*args, **kwargs)
        self.fields['PI']=forms.ModelChoiceField(queryset=Profile.objects.all())
        self.fields['CO_PI']=forms.ModelChoiceField(queryset=Profile.objects.all())"""

    class Meta:
        model = Event
        exclude = ['date_added']

        widgets = {
            'title': TextInput(attrs={
                'style': 'width: 100%;',
                'placeholder': 'Title'
                }),
            'venue' : TextInput(attrs={
                'style': 'width: 100%',
                'placeholder': 'Venue',
            }),
            'n_stud': NumberInput(attrs={
                'style': 'width: 100%;',
                'placeholder': 'No of students',
            }),
            'n_fac': NumberInput(attrs={
                'style': 'width: 100%;',
                'placeholder': 'No of faculty',
            }),
            'n_ind': NumberInput(attrs={
                'style': 'width: 100%;',
                'placeholder': 'No from industry',
            }),
            'date': SelectDateWidget(attrs={
                'style': 'width: 100%;',
                'placeholder': 'Date',
            }),
            'u_id': SelectMultiple(attrs={
                'style': 'width: 100%;',
                'placeholder': 'Faculty involved',
            }),
        }


class BookForm(forms.ModelForm):
    """def __init__(self, *args, **kwargs):
        user = kwargs.pop('user','')
        super(GrantForm, self).__init__(*args, **kwargs)
        self.fields['PI']=forms.ModelChoiceField(queryset=Profile.objects.all())
        self.fields['CO_PI']=forms.ModelChoiceField(queryset=Profile.objects.all())"""

    class Meta:
        model = Book
        exclude = ['date_added']

        widgets = {
            'n_isbn': NumberInput(attrs={
                'style': 'width: 100%;',
                'placeholder': 'ISBN #',
            }),
            'name': TextInput(attrs={
                'style': 'width: 100%;',
                'placeholder': 'Name of Book'
                }),
            'publisher' : TextInput(attrs={
                'style': 'width: 100%',
                'placeholder': 'Publisher',
            }),
            'u_id': SelectMultiple(attrs={
                'style': 'width: 100%;',
                'placeholder': 'Faculty involved',
            }),
        }


class WorkshopForm(forms.ModelForm):
    """def __init__(self, *args, **kwargs):
        user = kwargs.pop('user','')
        super(GrantForm, self).__init__(*args, **kwargs)
        self.fields['PI']=forms.ModelChoiceField(queryset=Profile.objects.all())
        self.fields['CO_PI']=forms.ModelChoiceField(queryset=Profile.objects.all())"""

    class Meta:
        model = Workshop
        exclude = ['date_added']

        widgets = {
            'event_name': TextInput(attrs={
                'style': 'width: 100%;',
                'placeholder': 'Name of the event'
                }),
            'venue' : TextInput(attrs={
                'style': 'width: 100%',
                'placeholder': 'Venue',
            }),
            'date': SelectDateWidget(attrs={
                'style': 'width: 100%;',
                'placeholder': 'Date of Event',
            }),
            
            'u_id': Select(attrs={
                'style': 'width: 100%;',
                'placeholder': 'Faculty involved',
            }),
        }


class MouForm(forms.ModelForm):
    """def __init__(self, *args, **kwargs):
        user = kwargs.pop('user','')
        super(GrantForm, self).__init__(*args, **kwargs)
        self.fields['PI']=forms.ModelChoiceField(queryset=Profile.objects.all())
        self.fields['CO_PI']=forms.ModelChoiceField(queryset=Profile.objects.all())"""

    class Meta:
        model = MoU
        exclude = ['date_added']

        widgets = {
            'organisation': TextInput(attrs={
                'style': 'width: 100%;',
                'placeholder': 'Organisation'
                }),
            'mod_col' : TextInput(attrs={
                'style': 'width: 100%',
                'placeholder': 'Mode of Collaboration',
            }),
            'validity': NumberInput(attrs={
                'style': 'width: 100%;',
                'placeholder': 'Validity',
            }),
            'date': SelectDateWidget(attrs={
                'style': 'width: 100%;',
                'placeholder': 'Date',
            }),
            'u_id': SelectMultiple(attrs={
                'style': 'width: 100%;',
                'placeholder': 'Faculty involved',
            }),
        }