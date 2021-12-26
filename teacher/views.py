
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

class ProposalCreateView(views.View,LoginRequiredMixin):
    login_url = '/login'
    redirect_field_name = 'login'

    def get(self,request):
        curr_user = request.user
        if not curr_user.is_teacher:
            logout(request)
            return redirect(reverse('login'))
        form = forms.ProposalForm
        return render(request,'teacher/teacher_proposal.html',{'form': form})
    def post(self,request):
        form = forms.ProposalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('teacher_proposal'))
        else:
            print('error')    
        
            return render(request,'teacher/teacher_proposal.html',{'form':form})

class ConsultancyCreateView(views.View,LoginRequiredMixin):
    login_url = '/login'
    redirect_field_name = 'login'

    def get(self,request):
        curr_user = request.user
        if not curr_user.is_teacher:
            logout(request)
            return redirect(reverse('login'))
        form = forms.ConsultancyForm
        return render(request,'teacher/teacher_consultancy.html',{'form': form})
    def post(self,request):
        form = forms.ConsultancyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('teacher_consultancy'))
        else:
            print('error')    
        
            return render(request,'teacher/teacher_consultancy.html',{'form':form})

class LectureCreateView(views.View,LoginRequiredMixin):
    login_url = '/login'
    redirect_field_name = 'login'

    def get(self,request):
        curr_user = request.user
        if not curr_user.is_teacher:
            logout(request)
            return redirect(reverse('login'))
        form = forms.LectureForm
        return render(request,'teacher/teacher_lecture.html',{'form': form})
    def post(self,request):
        form = forms.LectureForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('teacher_lecture'))
        else:
            print('error')    
        
            return render(request,'teacher/teacher_lecture.html',{'form':form})

class TalkCreateView(views.View,LoginRequiredMixin):
    login_url = '/login'
    redirect_field_name = 'login'

    def get(self,request):
        curr_user = request.user
        if not curr_user.is_teacher:
            logout(request)
            return redirect(reverse('login'))
        form = forms.TalkForm
        return render(request,'teacher/teacher_talk.html',{'form': form})
    def post(self,request):
        form = forms.TalkForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('teacher_talk'))
        else:
            print('error')    
        
            return render(request,'teacher/teacher_talk.html',{'form':form})

class ActivityCreateView(views.View,LoginRequiredMixin):
    login_url = '/login'
    redirect_field_name = 'login'

    def get(self,request):
        curr_user = request.user
        if not curr_user.is_teacher:
            logout(request)
            return redirect(reverse('login'))
        form = forms.ActivityForm
        return render(request,'teacher/teacher_activity.html',{'form': form})
    def post(self,request):
        form = forms.ActivityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('teacher_activity'))
        else:
            print('error')    
        
            return render(request,'teacher/teacher_activity.html',{'form':form})

class AchievementCreateView(views.View,LoginRequiredMixin):
    login_url = '/login'
    redirect_field_name = 'login'

    def get(self,request):
        curr_user = request.user
        if not curr_user.is_teacher:
            logout(request)
            return redirect(reverse('login'))
        form = forms.AchievementForm
        return render(request,'teacher/teacher_achievement.html',{'form': form})
    def post(self,request):
        form = forms.AchievementForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('teacher_achievement'))
        else:
            print('error')    
        
            return render(request,'teacher/teacher_achievement.html',{'form':form})

class ConferenceCreateView(views.View,LoginRequiredMixin):
    login_url = '/login'
    redirect_field_name = 'login'

    def get(self,request):
        curr_user = request.user
        if not curr_user.is_teacher:
            logout(request)
            return redirect(reverse('login'))
        form = forms.ConferenceForm
        return render(request,'teacher/teacher_conference.html',{'form': form})
    def post(self,request):
        form = forms.ConferenceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('teacher_conference'))
        else:
            print('error')    
        
            return render(request,'teacher/teacher_conference.html',{'form':form})

class IndustrialCreateView(views.View,LoginRequiredMixin):
    login_url = '/login'
    redirect_field_name = 'login'

    def get(self,request):
        curr_user = request.user
        if not curr_user.is_teacher:
            logout(request)
            return redirect(reverse('login'))
        form = forms.IndustrialForm
        return render(request,'teacher/teacher_industrial.html',{'form': form})
    def post(self,request):
        form = forms.IndustrialForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('teacher_industrial_visit'))
        else:
            print('error')    
        
            return render(request,'teacher/teacher_industrial.html',{'form':form})

class MembershipCreateView(views.View,LoginRequiredMixin):
    login_url = '/login'
    redirect_field_name = 'login'

    def get(self,request):
        curr_user = request.user
        if not curr_user.is_teacher:
            logout(request)
            return redirect(reverse('login'))
        form = forms.MembershipForm
        return render(request,'teacher/teacher_membership.html',{'form': form})
    def post(self,request):
        form = forms.MembershipForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('teacher_membership'))
        else:
            print('error')    
        
            return render(request,'teacher/teacher_membership.html',{'form':form})

class PatentCreateView(views.View,LoginRequiredMixin):
    login_url = '/login'
    redirect_field_name = 'login'

    def get(self,request):
        curr_user = request.user
        if not curr_user.is_teacher:
            logout(request)
            return redirect(reverse('login'))
        form = forms.PatentForm
        return render(request,'teacher/teacher_patent.html',{'form': form})
    def post(self,request):
        form = forms.PatentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('teacher_patent'))
        else:
            print('error')    
        
            return render(request,'teacher/teacher_patent.html',{'form':form})
