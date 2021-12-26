from django.urls import include, path, re_path
from . import views

urlpatterns = [
    path('home/',views.TeacherDashboard.as_view(),name='teacher_home'),
    path('report/grants/',views.GrantCreateView.as_view(),name='teacher_grant'),
    path('report/event/',views.EventCreateView.as_view(),name='teacher_event'),
    path('report/book/',views.BookCreateView.as_view(),name='teacher_book'),
    path('report/workshop/',views.WorkshopCreateView.as_view(),name='teacher_workshop'),
    path('report/mou/',views.MouCreateView.as_view(),name='teacher_mou'),
    path('report/proposal/',views.ProposalCreateView.as_view(),name='teacher_proposal'),
    path('report/consultancy/',views.ConsultancyCreateView.as_view(),name='teacher_consultancy'),
    path('report/lecture/',views.LectureCreateView.as_view(),name='teacher_lecture'),
    path('report/talk/',views.TalkCreateView.as_view(),name='teacher_talk'),
    path('report/other-activity/',views.ActivityCreateView.as_view(),name='teacher_activity'),
    path('report/achievement/',views.AchievementCreateView.as_view(),name='teacher_achievement'),
    path('report/conference/',views.ConferenceCreateView.as_view(),name='teacher_conference'),
    path('report/industrial-visit/',views.IndustrialCreateView.as_view(),name='teacher_industrial_visit'),
    path('report/membership/',views.MembershipCreateView.as_view(),name='teacher_membership'),
    path('report/patent/',views.PatentCreateView.as_view(),name='teacher_patent'),
]