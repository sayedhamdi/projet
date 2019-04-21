from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser,Condidature,InfoSession

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'email','cin','birthDate','image','first_name','last_name')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email','cin','birthDate','image','first_name','last_name')

class CondidatureForm(forms.ModelForm):
    class Meta:
        model = Condidature
        fields = ('etablissement','fichiers')

class InfosessionForm(forms.ModelForm):
    class Meta:
        model = InfoSession
        fields = ('etablissement','date','fichier_autorisation')
