from django import forms
from django.forms import widgets
from django.forms.widgets import PasswordInput
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

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


    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        r = User.objects.filter(email=email)
        if r.count():
            self._errors['email'] = self.error_class(['Username already exists!!'])
        dom_name = email.split('@')[1]
        if dom_name!='rvce.edu.in':
            self._errors['email'] = self.error_class(['You must use an RVCE email address!!'])
            #raise  ValidationError("Email already exists")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError("Password don't match")

        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user