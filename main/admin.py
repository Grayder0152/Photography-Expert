from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug')
    list_display_links = ('title',)
    readonly_fields = ('id', 'title', 'slug')


@admin.register(Images)
class Images(admin.ModelAdmin):
    """Фотографии"""
    list_display = ('__str__', 'get_big_image', 'get_small_image')
    list_filter = ('category',)

    def get_big_image(self, obj):
        return mark_safe(f'<img src={obj.big_image.url} width="80" height="auto" >')

    def get_small_image(self, obj):
        if obj.small_image:
            return mark_safe(f'<img src={obj.small_image.url} width="80" height="auto" >')
        return 'Не загружена'

    get_big_image.short_description = "Большое зображение"
    get_small_image.short_description = "Маленькое зображение"


admin.site.site_title = 'Photography-Expert | Administration panel'
admin.site.site_header = 'Photography-Expert | Administration panel'
