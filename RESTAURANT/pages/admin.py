from django.contrib import admin
from django.utils.html import format_html
from .models import MenuItem

class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'show_image')
    search_fields = ('name',)

    def show_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="80" height="80" />', obj.image.url)
        return "No Image"
    show_image.short_description = "Image"

admin.site.register(MenuItem, MenuItemAdmin)
