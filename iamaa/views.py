from django.shortcuts import render
from django.utils import timezone
from .models import Welcome, ArtistIntroduction


# Create your views here.
def home(request):  ## rename to match imaa
    #artist = ArtistIntroduction.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    welcome_text = Welcome.objects.all()
    return render(request, 'iamaa/home.html' , {'welcome_text' : welcome_text})

def about(request):
    return render(request,'iamaa/aboutpage.html')
