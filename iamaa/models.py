from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.

class ArtistIntroduction(models.Model):
    # interview_video = video is here either upload or reference from url 
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def add_video(self):
        pass

    def add_comment(self):
        pass

    def __str__(self):
        return self.title


class Comment(models.Model):
    text = models.TextField()
    created_date =  models.DateTimeField(default=timezone.now)

    def publish(self):
        self.published_date = timezone.now()
        self.save()




class Welcome(models.Model):
    text = models.TextField()
