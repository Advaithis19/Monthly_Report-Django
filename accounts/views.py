from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from django import views
from django.http import response
from django.shortcuts import redirect, render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, get_user_model, logout
from django.urls import reverse, reverse_lazy
from . import forms
from django.contrib import messages

UserModel = get_user_model()
# Create your views here.
class RegisterStudent(views.View):
    def get(self, request):
        form = forms.CreateUserForm
        return render(request, 'registration/signup.html', {'form':form})

    def post(self, request):
        form = forms.CreateUserForm(request.POST)
        if request.method == "POST":
            if form.is_valid():
                email = form.cleaned_data['email']
                pwd = form.cleaned_data['password']
                role = request.POST['role']
                print(role)

                if(role=="teacher"):
                    user = UserModel.objects.create_teacheruser(
                        email=email,
                        password=pwd
                    )
                elif(role=="admin"):
                    user = UserModel.objects.create_adminuser(
                        email=email,
                        password=pwd
                    )
                elif(role=="superadmin"):
                    user = UserModel.objects.create_superadminuser(
                        email=email,
                        password=pwd
                    )

                #form.save()
        return(redirect(reverse('signup')))

class LoginPage(views.View):
    def get(self, request):
        form = forms.LoginForm
        return render(request, 'registration/login.html', {'form': form})
    
    def post(self, request):
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            email   = form.cleaned_data['email']
            pwd     = form.cleaned_data['password']
            user = authenticate(username=email, password=pwd)
            print(str(user))
            if user is not None:
                login(request, user)
                curr_user = request.user

                if curr_user.is_teacher:
                    return redirect(reverse('teacher_home'))
                if curr_user.is_admin:
                    return redirect(reverse('admin_home'))
                if curr_user.is_superadmin:
                    return redirect(reverse('sadmin_home'))
                    
            else:
                if UserModel.objects.filter(email=email).exists():
                    messages.error(request, 'Incorrect username or password')
                else:
                    messages.error(request, 'This user does not exist. Please register')   
                return(render(request, 'registration/login.html', {'form':form}))
        else:
            messages.error(request, 'email did not pass validation')
            return(redirect('login'))

def home(request):
    return render(request, 'registration/home.html')

def logout_view(request):
    logout(request)
    return(redirect(reverse('home')))
