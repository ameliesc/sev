from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from . import views

urlpatterns = [
    path(r'', views.home, name='home'),
    path(r'',views.about, name='aboutpage')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
