from django.contrib import admin
from . import models
from django.utils.safestring import mark_safe

# Register your models here.
@admin.register(models.Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display = ('nom', 'date_update', 'date_add', 'status')
    list_editable = ('status',) 

@admin.register(models.Produit)
class ProduitAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prix', 'images_view', 'quantite', 'couleur', 'date_update', 'date_add', 'status')
    list_editable = ('status',)

    def images_view(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" style="height:50px; width:100px">')
    images_view.short_description = 'Aperçu des images'

@admin.register(models.Commande)
class CommandeAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'nom_compagnie', 'email', 'address', 'ville', 'code', 'telephone', 'date_update', 'date_add', 'status')
    list_editable = ('status',)

@admin.register(models.ImageArticle)
class ImageArticleAdmin(admin.ModelAdmin):
    list_display = ('images_view', 'date_update', 'date_add', 'status')
    list_editable = ('status',)

    def images_view(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" style="height:50px; width:100px">')
    images_view.short_description = 'Aperçu des images'


@admin.register(models.Marque)
class MarqueAdmin(admin.ModelAdmin):
    list_display = ('nom', 'date_update', 'date_add', 'status')
    list_editable = ('status',)

@admin.register(models.Couleur)
class CouleurAdmin(admin.ModelAdmin):
    list_display = ('nom', 'date_update', 'date_add', 'status')
    list_editable = ('status',)
