
from django import views
from django.http import response
from django.shortcuts import redirect, render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, get_user_model, logout
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin

from api.models import Grants
from . import forms

# Create your views here.
class TeacherDashboard(LoginRequiredMixin,views.View):
    login_url = '/login'
    redirect_field_name = 'login'
    def get(self,request):
        curr_user = request.user
        if not curr_user.is_teacher:
            logout(request)
            return redirect(reverse('login'))
        return(render(request,'teacher/teacher_home.html'))

class GrantCreateView(views.View,LoginRequiredMixin):
    login_url = '/login'
    redirect_field_name = 'login'

    def get(self,request):
        curr_user = request.user
        if not curr_user.is_teacher:
            logout(request)
            return redirect(reverse('login'))
        form = forms.GrantForm
        return render(request,'teacher/teacher_grant.html',{'form': form})
    def post(self,request):
        form = forms.GrantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('teacher_grant'))
        else:
            print('error')    
        
            return render(request,'teacher/teacher_grant.html',{'form':form})

class EventCreateView(views.View,LoginRequiredMixin):
    login_url = '/login'
    redirect_field_name = 'login'

    def get(self,request):
        curr_user = request.user
        if not curr_user.is_teacher:
            logout(request)
            return redirect(reverse('login'))
        form = forms.EventForm
        return render(request,'teacher/teacher_event.html',{'form': form})
    def post(self,request):
        form = forms.EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('teacher_event'))
        else:
            print('error')    
        
            return render(request,'teacher/teacher_event.html',{'form':form})

class BookCreateView(views.View,LoginRequiredMixin):
    login_url = '/login'
    redirect_field_name = 'login'

    def get(self,request):
        curr_user = request.user
        if not curr_user.is_teacher:
            logout(request)
            return redirect(reverse('login'))
        form = forms.BookForm
        return render(request,'teacher/teacher_book.html',{'form': form})
    def post(self,request):
        form = forms.BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('teacher_book'))
        else:
            print('error')    
        
            return render(request,'teacher/teacher_book.html',{'form':form})

class WorkshopCreateView(views.View,LoginRequiredMixin):
    login_url = '/login'
    redirect_field_name = 'login'

    def get(self,request):
        curr_user = request.user
        if not curr_user.is_teacher:
            logout(request)
            return redirect(reverse('login'))
        form = forms.WorkshopForm
        return render(request,'teacher/teacher_workshop.html',{'form': form})
    def post(self,request):
        form = forms.WorkshopForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('teacher_workshop'))
        else:
            print('error')    
        
            return render(request,'teacher/teacher_workshop.html',{'form':form})

class MouCreateView(views.View,LoginRequiredMixin):
    login_url = '/login'
    redirect_field_name = 'login'

    def get(self,request):
        curr_user = request.user
        if not curr_user.is_teacher:
            logout(request)
            return redirect(reverse('login'))
        form = forms.MouForm
        return render(request,'teacher/teacher_mou.html',{'form': form})
    def post(self,request):
        form = forms.MouForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('teacher_mou'))
        else:
            print('error')    
        
            return render(request,'teacher/teacher_mou.html',{'form':form})
