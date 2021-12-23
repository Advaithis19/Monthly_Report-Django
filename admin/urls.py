from django.urls import include, path, re_path

from admin.views import GrantView
from . import views

urlpatterns = [
    path('home/',views.AdminDashboard.as_view(),name='admin_home'),
    path('report/grant/',views.GrantView.as_view(),name ='admin_grant'),
    path('report/event/',views.EventView.as_view(),name ='admin_event'),
    path('report/book/',views.BookView.as_view(),name ='admin_book'),
    path('report/workshop/',views.WorkshopView.as_view(),name ='admin_workshop'),
    path('report/mou/',views.MouView.as_view(),name ='admin_mou')
]