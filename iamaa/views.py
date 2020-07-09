import os
from django.conf import settings
from django.shortcuts import render
from django.utils import timezone
from .models import Description, Welcome

# Create your views here.
def home(request):  ## rename to match imaa
    #artist = ArtistIntroduction.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    welcome_text = Welcome.objects.all()
    description = Description.objects.all()



    return render(request, 'index.html' , {'welcome_text' : welcome_text,  'sev_sessions': description})

def about(request):
    return render(request,'iamaa/aboutpage.html')
