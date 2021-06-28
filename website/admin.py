from django.contrib import admin
from . import models
from django.utils.safestring import mark_safe

# Register your models here.
@admin.register(models.Website)
class WebsiteAdmin(admin.ModelAdmin):
    list_display = ('nom', 'images_view', 'date_update', 'date_add', 'status')
    list_editable = ('status',)

    def images_view(self, obj):
        return mark_safe(f'<img src="{obj.logo.url}" style="height:50px; width:100px">')

    images_view.short_description = 'Aperçu des images'


@admin.register(models.Newletter)
class NewletterAdmin(admin.ModelAdmin):
    list_display = ('email', 'date_update', 'date_add', 'status')
    list_editable = ('status',)

@admin.register(models.Configuration)
class ConfigurationAdmin(admin.ModelAdmin):
    list_display = ('copyrights', 'date_update', 'date_add', 'status')
    list_editable = ('status',)

@admin.register(models.SocialIcon)
class SocialIconAdmin(admin.ModelAdmin):
    list_display = ('nom', 'icone', 'lien', 'date_update', 'date_add', 'status')
    list_editable = ('status',)
