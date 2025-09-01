from django.contrib import admin
from .models import Collection, Image

# Register your models here.
@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ('name', 'user')

 


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('unsplash_id', 'url', 'description')