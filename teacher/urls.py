from django.urls import include, path, re_path
from . import views

urlpatterns = [
    path('home/',views.TeacherDashboard.as_view(),name='teacher_home'),
    path('report/grants/',views.GrantCreateView.as_view(),name='teacher_grant'),
    path('report/event/',views.EventCreateView.as_view(),name='teacher_event'),
    path('report/book/',views.BookCreateView.as_view(),name='teacher_book'),
    path('report/workshop/',views.WorkshopCreateView.as_view(),name='teacher_workshop'),
    path('report/mou/',views.MouCreateView.as_view(),name='teacher_mou')
]