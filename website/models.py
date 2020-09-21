from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Contact(models.Model):
    nom = models.CharField(max_length = 255)
    email = models.EmailField()
    sujet = models.CharField(max_length = 255)
    message = models.TextField()

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now = True)
    status = models.BooleanField(default = True)

    class Meta:
        verbose_name ="contact"
        verbose_name_plural = "contacts"

    def __str__(self):
        return self.nom 

class NewsLetter(models.Model):
    email = models.EmailField()

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now = True)
    status = models.BooleanField(default = True)

    class Meta:
        verbose_name ="newsLetter"
        verbose_name_plural = "newsletters"

    def __str__(self):
        return str(self.email)    

class SiteInfo(models.Model):
    map_url = models.TextField()
    email = models.EmailField()

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now = True)
    status = models.BooleanField(default = True)

    class Meta:
        verbose_name ="Site Info"
        verbose_name_plural = "Site Infos"

    def __str__(self):
        return self.email

class Presentation(models.Model):
    nom = models.CharField(max_length = 255)
    description = models.TextField()
    image = models.ImageField(upload_to='images/Produit')

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now = True)
    status = models.BooleanField(default = True)

    class Meta:
        verbose_name ="Presentation"
        verbose_name_plural = "Presentations"

    def __str__(self):
        return self.nom 

        

class UserAccount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to="images/User", default='images/avatar.png')

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'UserAccount'
        verbose_name_plural = 'UserAccounts'

    def __str__(self):
        return str(self.user)


class OtherInfo(models.Model):
    addresse = models.CharField(max_length=255)
    contact = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    site = models.CharField(max_length=50)

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'Autre'
        verbose_name_plural = 'Autres'

    def __str__(self):
        return str(self.addresse)