from django.contrib import admin
from .models import Album,Song,Blog

# Register your models here.s

admin.site.register(Album)
admin.site.register(Song)
admin.site.register(Blog)