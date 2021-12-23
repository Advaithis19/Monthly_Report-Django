from django.urls import include, path, re_path
from . import views

urlpatterns = [
    path('home/',views.SadminDashboard.as_view(),name='sadmin_home'),
    path('report/grant/',views.GrantView.as_view(),name ='sadmin_grant'),
    path('report/event/',views.EventView.as_view(),name ='sadmin_event'),
    path('report/book/',views.BookView.as_view(),name ='sadmin_book'),
    path('report/workshop/',views.WorkshopView.as_view(),name ='sadmin_workshop'),
    path('report/mou/',views.MouView.as_view(),name ='sadmin_mou')
]