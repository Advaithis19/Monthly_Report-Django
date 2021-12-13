from django.shortcuts import redirect, render
from django.urls.base import reverse

from api.models import Profile

# Create your views here.
def home(request):
    return(render(request,'sadmin/sadmin_home.html'))

