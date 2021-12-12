from django.contrib import admin
<<<<<<< HEAD
from .models import CustomUser
# Register your models here.
admin.site.register(CustomUser)
=======
from django.contrib.auth import get_user_model

User = get_user_model()
admin.site.register(User)
>>>>>>> 9b51d7eb23f560383398afb298c6d27f023a969c
