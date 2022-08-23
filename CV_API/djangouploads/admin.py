from django.contrib import admin
from .models import ImageInfo
from .models import Drink



class ImageInfoAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)


admin.site.register(ImageInfo, ImageInfoAdmin)
admin.site.register(Drink)