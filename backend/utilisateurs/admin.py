from django.contrib import admin
from .models import Utilisateur
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

@admin.register(Utilisateur)
class UtilisateurAdmin(BaseUserAdmin):
    list_display = ("username", 'email','first_name', 'last_name', )
    search_fields = ('username', 'email')
    ordering = ('id',)