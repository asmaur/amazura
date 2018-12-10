from django.contrib import admin
from django.utils.html import format_html
from .models import *
# Register your models here.
@admin.register(Terapeuta)
class TerapeutasAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="{}" height="30" width="30" />'.format(obj.capa.url))

    image_tag.short_description = 'Image'

    list_display = ('fullname', 'idade', 'peso', 'altura', 'is_working', 'code', 'image_tag', 'created')
    fields = ['first_name', 'last_name', 'idade', 'peso', 'altura', 'capa', 'telefone', 'texto', 'is_working',]


class PhotoInline(admin.StackedInline):
    model = Photo
    extra = 1

@admin.register(Album)
class AlbumManager(admin.ModelAdmin):
    list_display = ('title', 'terapeuta', 'is_visible', 'code', 'created')
    fields = ['title', 'terapeuta', 'is_visible']

    def save_model(self, request, obj, form, change):
        obj.save()
        for afile in request.FILES.getlist('photos_multiple'):
            obj.photos.create(image=afile)


@admin.register(Photo)
class PhotoManager(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="{}" height="30" width="30" />'.format(obj.image.url))

    image_tag.short_description = 'Image'

    list_display = ('code', 'album', 'valor', 'is_public', 'image_tag','date_added')
    fields = ['image', 'album', 'valor', 'is_public']
    #list_filter = ['is_visible']






#admin.site.register(Terapeuta, TerapeutasAdmin)
#admin.site.register(Album)
#admin.site.register(Photo)