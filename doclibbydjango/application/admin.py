
# Register your models here.
from django.contrib import admin
from .models import UserHealthData  # Remplacez par vos noms de modèles

# admin.site.register(UserHealthData)

class colonnes(admin.ModelAdmin):
    #list_display = ("id", "username", "role", "email","is_superuser",)  #[field.name for field in Utilisateur._meta.get_fields()]
    list_display = [field.name for field in UserHealthData._meta.get_fields()]

admin.site.register(UserHealthData, colonnes)

