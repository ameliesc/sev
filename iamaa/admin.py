from django.contrib import admin

# Register your models here.
from .models import ArtistIntroduction, Comment, Welcome



class HomeAdmin(admin.ModelAdmin):
  def has_add_permission(self, request):
    num_objects = self.model.objects.count()
    if num_objects >= 1:
      return False
    else:
      return True


admin.site.register(Welcome, HomeAdmin)
#admin.site.register(Welcome)
