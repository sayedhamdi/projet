from django.contrib.auth.models import AbstractUser
from django.db import models
import datetime


class Reunion(models.Model):
    date = models.DateTimeField()
    place = models.CharField(max_length=100)


class CustomUser(AbstractUser):
    # add additional fields in here
    birthDate = models.DateField(default=datetime.date.today,blank=True)
    cin = models.IntegerField(blank=True,null=True)
    image = models.ImageField(default='no image',blank=True)
    reunions = models.ManyToManyField(Reunion,blank=True,related_name="reunions")
    def __str__(self):
        return self.email

class Condidature(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name="userCondidat",null=True)
    isAccepted = models.BooleanField(default=False)
    etablissement = models.CharField(max_length=64)
    fichiers = models.FileField()

class InfoSession(models.Model):
    #najem nrod el etablissement class wa7adha w feha nom etab adresse et url site
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name="userInfosession",null=True)
    etablissement = models.CharField(max_length=64)
    date = models.DateTimeField()
    #fichier autorisation heya taswira yekhoha el etudiant li bech yaamel infossion el document d'autorisation mel idara
    fichier_autorisation = models.FileField()
