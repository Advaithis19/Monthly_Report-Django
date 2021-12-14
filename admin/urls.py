from django.urls import include, path, re_path

from admin.views import GrantView
from . import views

urlpatterns = [
    path('home/',views.AdminDashboard.as_view(),name='admin_home'),
    path('report/grant/',views.GrantView.as_view(),name ='admin_grant')
]