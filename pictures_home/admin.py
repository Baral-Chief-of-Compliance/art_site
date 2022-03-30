from django.contrib import admin

# Register your models here.

from pictures_home.models import Artist, Picture



admin.site.register(Artist)
admin.site.register(Picture)