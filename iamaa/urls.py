from django.urls import path
from . import views

urlpatterns = [
    path(r'', views.home, name='home'),
    path(r'',views.about, name='aboutpage')
]
