from django.contrib.auth.models import AbstractUser
from django.db import models
import datetime
class Condidature(models.Model):
    isAccepted = models.BooleanField()
    etablissement = models.CharField(max_length=64)
    fichiers = models.FileField(null=True)
    def __str__(self):
        return f"- {self.etablissement}"

class Reunion(models.Model):
    date = models.DateTimeField()
    place = models.CharField(max_length=100)


class InfoSession(models.Model):
    #najem nrod el etablissement class wa7adha w feha nom etab adresse et url site
    etablissement = models.CharField(max_length=64)
    date = models.DateTimeField()
    #fichier autorisation heya taswira yekhoha el etudiant li bech yaamel infossion el document d'autorisation mel idara
    fichier_autorisation = models.FileField()

class CustomUser(AbstractUser):
    # add additional fields in here
    birthDate = models.DateField(default=datetime.date.today,blank=True)
    cin = models.IntegerField(blank=True,null=True)
    image = models.ImageField(default='no image',blank=True)
    condidatures = models.ManyToManyField(Condidature,related_name="user")
    reunions = models.ForeignKey(Reunion,null=True,related_name="reunions",on_delete=models.CASCADE)
    infoSessions = models.ForeignKey(InfoSession,null=True,related_name="infoSessions",on_delete=models.CASCADE)
    def __str__(self):
        return self.email
    def addCondidature(self,condidature):
        self.condidature=condidature
