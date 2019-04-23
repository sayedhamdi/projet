from django.contrib import admin
from .models import CustomUser,Condidature,InfoSession,Reunion
# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Condidature)
admin.site.register(InfoSession)
admin.site.register(Reunion)
