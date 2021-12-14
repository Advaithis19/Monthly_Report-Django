
from django import views
from django.http import response
from django.shortcuts import redirect, render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, get_user_model, logout
from django.urls import reverse, reverse_lazy

from api.models import Grants
from . import forms

# Create your views here.
def home(request):
    return(render(request,'teacher/teacher_home.html'))

class GrantView(views.View):
    def get(self,request):
        form = forms.GrantForm
        return render(request,'teacher/teacher_grant.html',{'form': form})
    def post(self,request):
        form = forms.GrantForm(request.POST)
        if form.is_valid():
            form.save()
            """title = form.cleaned_data['title']
            agency = form.cleaned_data['agency']
            sanc_amt = form.cleaned_data['sanc_amt']
            year = form.cleaned_data['year']
            remarks = form.cleaned_data['remarks']
            PI = form.cleaned_data['PI']
            CO_PI = form.cleaned_data['CO_PI']
            date_added = form.cleaned_data['date_added']
            Grants.objects.create(title = title,agency = agency,sanc_amt = sanc_amt, year = year, remarks = remarks, date_added = date_added,PI = PI,CO_PI = CO_PI)"""
            return redirect(reverse('teacher_grant'))
        else:
            print('error')    
        
        return render(request,'teacher/teacher_grant.html',{'form':form})
