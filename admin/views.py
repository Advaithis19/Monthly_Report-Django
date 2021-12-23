from django.shortcuts import render

from django import views
from django.http import response
from django.shortcuts import redirect, render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, get_user_model, logout
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from api.models import *
from . import forms
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class AdminDashboard(LoginRequiredMixin,views.View):
    login_url = '/login'
    redirect_field_name = 'login'

    def get(self,request):
        curr_user = request.user
        if not curr_user.is_admin:
            logout(request)
            return redirect(reverse('login'))
        return(render(request,'admin/admin_home.html'))

class GrantView(LoginRequiredMixin,views.View):
    login_url = '/login'
    redirect_field_name = 'login'
    def get(self,request):
        curr_user = request.user
        if not curr_user.is_admin:
            logout(request)
            return redirect(reverse('login'))
        form = forms.DateForm
        return render(request,'admin/admin_grant.html',{'form':form})
        
    def post(self,request):
        form = forms.DateForm(request.POST)
        if form.is_valid():
            month = form.cleaned_data['month']
            year = form.cleaned_data['year']
            curr_user = request.user
            user_profile = Profile.objects.get(user = curr_user)
            dept = user_profile.department
            month_grants = Grants.objects.filter(
                date_added__year = year,
                date_added__month = month
            )
            for grant in month_grants:
                if dept!=grant.PI.department:
                    month_grants = month_grants.exclude(PI = grant.PI)
            
        return render(request,'admin/admin_grant.html',{'data': month_grants,'form':form})

class EventView(LoginRequiredMixin,views.View):
    login_url = '/login'
    redirect_field_name = 'login'
    def get(self,request):
        curr_user = request.user
        if not curr_user.is_admin:
            logout(request)
            return redirect(reverse('login'))
        form = forms.DateForm
        return render(request,'admin/admin_event.html',{'form':form})
        
    def post(self,request):
        form = forms.DateForm(request.POST)
        if form.is_valid():
            month = form.cleaned_data['month']
            year = form.cleaned_data['year']
            curr_user = request.user
            user_profile = Profile.objects.get(user = curr_user)
            dept = user_profile.department
            month_events = Event.objects.filter(
                date_added__year = year,
                date_added__month = month
            )
            for event in month_events:
                for faculty in event.u_id.all():
                    dept_found = False
                    if dept==faculty.department:
                        dept_found=True
                    if not dept_found:
                        month_events = month_events.exclude(u_id = faculty)

        return render(request,'admin/admin_event.html',{'data': month_events,'form':form})

class BookView(LoginRequiredMixin,views.View):
    login_url = '/login'
    redirect_field_name = 'login'
    def get(self,request):
        curr_user = request.user
        if not curr_user.is_admin:
            logout(request)
            return redirect(reverse('login'))
        form = forms.DateForm
        return render(request,'admin/admin_book.html',{'form':form})
        
    def post(self,request):
        form = forms.DateForm(request.POST)
        if form.is_valid():
            month = form.cleaned_data['month']
            year = form.cleaned_data['year']
            curr_user = request.user
            user_profile = Book.objects.get(user = curr_user)
            dept = user_profile.department
            month_books = Grants.objects.filter(
                date_added__year = year,
                date_added__month = month
            )
            for book in month_books:
                for faculty in book.u_id.all():
                    dept_found = False
                    if dept==faculty.department:
                        dept_found=True
                    if not dept_found:
                        month_books = month_books.exclude(u_id = faculty)
            
        return render(request,'admin/admin_book.html',{'data': month_books,'form':form})

class WorkshopView(LoginRequiredMixin,views.View):
    login_url = '/login'
    redirect_field_name = 'login'
    def get(self,request):
        curr_user = request.user
        if not curr_user.is_admin:
            logout(request)
            return redirect(reverse('login'))
        form = forms.DateForm
        return render(request,'admin/admin_workshop.html',{'form':form})
        
    def post(self,request):
        form = forms.DateForm(request.POST)
        if form.is_valid():
            month = form.cleaned_data['month']
            year = form.cleaned_data['year']
            curr_user = request.user
            user_profile = Profile.objects.get(user = curr_user)
            dept = user_profile.department
            month_workshops = Workshop.objects.filter(
                date_added__year = year,
                date_added__month = month
            )
            for workshop in month_workshops:
                for faculty in workshop.u_id.all():
                    dept_found = False
                    if dept==faculty.department:
                        dept_found=True
                    if not dept_found:
                        month_workshops = month_workshops.exclude(u_id = faculty)
            
        return render(request,'admin/admin_workshop.html',{'data': month_workshops,'form':form})

class MouView(LoginRequiredMixin,views.View):
    login_url = '/login'
    redirect_field_name = 'login'
    def get(self,request):
        curr_user = request.user
        if not curr_user.is_admin:
            logout(request)
            return redirect(reverse('login'))
        form = forms.DateForm
        return render(request,'admin/admin_mou.html',{'form':form})
        
    def post(self,request):
        form = forms.DateForm(request.POST)
        if form.is_valid():
            month = form.cleaned_data['month']
            year = form.cleaned_data['year']
            curr_user = request.user
            user_profile = Profile.objects.get(user = curr_user)
            dept = user_profile.department
            month_mous = MoU.objects.filter(
                date_added__year = year,
                date_added__month = month
            )
            for mou in month_mous:
                for faculty in mou.u_id.all():
                    dept_found = False
                    if dept==faculty.department:
                        dept_found=True
                    if not dept_found:
                        month_mous = month_mous.exclude(u_id = faculty)
            
        return render(request,'admin/admin_mou.html',{'data': month_mous,'form':form})