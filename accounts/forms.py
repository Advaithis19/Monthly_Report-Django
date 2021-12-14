from django import forms
from django.db.models import fields
from django.forms import widgets
from django.forms.widgets import PasswordInput, Select, TextInput
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.http import request
from api.models import Profile

class LoginForm(forms.Form):
    email       = forms.EmailField(max_length=255, required=True, widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    password    = forms.CharField(required=True, widget=PasswordInput(attrs={'placeholder':'Password'}))

User = get_user_model()

class CreateUserForm(forms.ModelForm):

    CHOICES = [
        ('teacher','Teacher'),
        ('admin','HoD/Department Admin'),
        ('superadmin','Principal/Dean')
    ]
    email       = forms.EmailField(max_length=255, required=True, widget=forms.EmailInput(attrs={'placeholder':'Email'}))
    password    = forms.CharField(max_length=255, required=True, widget=forms.PasswordInput(attrs={'placeholder' : 'Password'}))
    password2   = forms.CharField(max_length=255, required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}))
    role = forms.CharField(label='What is your role?', widget=forms.RadioSelect(choices=CHOICES))

    class Meta:
        model = User
        fields=("email","password","password2","role")


    def clean(self):
        super(CreateUserForm, self).clean()

        email = self.cleaned_data['email'].lower()
        dom_name = email.split('@')[1]
        if dom_name!='rvce.edu.in':
            raise ValidationError('You must use an RVCE email address!!',code='invalid')
            #raise  ValidationError("Email already exists")

        password1 = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")

        return self.cleaned_data

        

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user


class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        exclude = ['user']

        
        widgets = {
            'fname': TextInput(attrs={
                'style': 'width: 100%;',
                'placeholder': 'Full Name'
                }),
            'mname' : TextInput(attrs={
                'style': 'width: 100%',
                'placeholder': 'Middle Name',
            }),
            'lname': TextInput(attrs={
                'style': 'width: 100%;',
                'placeholder': 'Last Name',
            }),
            'uname': TextInput(attrs={
                'style': 'width: 100%;',
                'placeholder': 'Username',
            }),
            'department': Select(attrs={
                'style': 'width: 100%;',
                'placeholder': 'Department',
            })
        }

