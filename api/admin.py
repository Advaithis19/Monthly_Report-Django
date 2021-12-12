from django.contrib import admin
from .models import Achievement, Book, Conference, Consultancy, Event, Grants, Industrial_visit, Lecture, Membership, MoU, Other_Activity, Patent, Profile, Proposal, Talk, Workshop

admin.site.register(Profile)
admin.site.register(Grants)
admin.site.register(Proposal)
admin.site.register(Talk)
admin.site.register(Workshop)
admin.site.register(Consultancy)
admin.site.register(Lecture)
admin.site.register(Event)
admin.site.register(Other_Activity)
admin.site.register(Achievement)
admin.site.register(Conference)
admin.site.register(MoU)
admin.site.register(Patent)
admin.site.register(Industrial_visit)
admin.site.register(Membership)
admin.site.register(Book)
