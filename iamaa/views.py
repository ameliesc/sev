from django.shortcuts import render
from django.utils import timezone
from .models import ArtistIntroduction
# Create your views here.
def posts(request):  ## rename to match imaa
    artist = ArtistIntroduction.objects.filter(published_date__lte=timezone.now()).order_by('published_date')

    return render(request, 'iamaa/imaa.html')


