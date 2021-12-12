from django.urls import include, path, re_path
from . import views

urlpatterns = [
    re_path(r'^signup/*', views.RegisterStudent.as_view(), name = 'signup'),
    path('login/',views.LoginPage.as_view(), name = 'login'),
    path('logout/',views.logout_view, name='logout'),
    path('', views.home,name = 'home')
]