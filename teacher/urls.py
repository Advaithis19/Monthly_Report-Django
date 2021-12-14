from django.urls import include, path, re_path
from . import views

urlpatterns = [
    path('home/',views.TeacherDashboard.as_view(),name='teacher_home'),
    path('report/grant/',views.GrantView.as_view(),name='teacher_grant')
]