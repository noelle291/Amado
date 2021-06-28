from django.db import models

# Create your models here.

class Categorie(models.Model):
    nom =  models.CharField(max_length=255)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'Categorie'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.nom 

class Produit(models.Model):
    nom = models.CharField(max_length=255)
    prix = models.IntegerField(default=0)
    image = models.FileField(upload_to="produit_image")
    description = models.TextField()
    quantite = models.IntegerField(default=0)
    categorie = models.ForeignKey("prestation.Categorie", related_name="categorie_article", on_delete=models.CASCADE)
    marque = models.ForeignKey( "prestation.Marque", related_name="Marque_article", on_delete=models.CASCADE)
    couleur = models.CharField(max_length=255)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'Produit'
        verbose_name_plural = 'Produits'

    def __str__(self):
        return self.nom


class Commande(models.Model):
    nom =  models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    nom_compagnie =  models.CharField(max_length=255)
    email = models.EmailField()
    pays = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    ville = models.CharField(max_length=255)
    code = models.CharField(max_length=255)
    telephone = models.CharField(max_length=255)
    commentaire = models.TextField()
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'Commande'
        verbose_name_plural = 'Commandes'

    def __str__(self):
        return self.nom


class ImageArticle(models.Model):
    image = models.FileField(upload_to="produit_image")
    produit = models.ForeignKey("prestation.Produit", related_name="images_produit", on_delete=models.CASCADE)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'ImageArticle'
        verbose_name_plural = 'ImageArticles'

    def __str__(self):
        return f"{self.image}"


class Marque(models.Model):
    nom =  models.CharField(max_length=255)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'Marque'
        verbose_name_plural = 'Marques'

    def __str__(self):
        return self.nom


class Couleur(models.Model):
    nom =  models.CharField(max_length=255)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'Couleur'
        verbose_name_plural = 'Couleurs'

    def __str__(self):
        return self.nom
