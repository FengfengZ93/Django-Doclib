from django.db import models
from django.contrib.auth.models import AbstractUser

class Utilisateur(AbstractUser):
    patient = "patient"
    medecin = "medecin"
    responsable = "responsable"
    # first_login = models.BooleanField(default=True)

    lesRoles = (
        ('patient', 'patient'),
        ('medecin', 'medecin'),
        ('responsable', 'responsable')
    )
    role = models.CharField(max_length=30,
                            choices=lesRoles,
                            verbose_name='Role', null=True)

# Trop long, la flemme
# class Connexion(models.Model):
#     username = models.CharField(max_length=50)
#     motDePasse = models.CharField(max_length=50)

class medecinPatient(models.Model):
    idPatient = models.ForeignKey(Utilisateur, 
                                  null=True, 
                                  on_delete=models.SET_NULL,
                                  related_name='patientMedecin',
                                  unique=True)
    idMedecin = models.ForeignKey(Utilisateur,
                                  null=True,
                                  on_delete=models.SET_NULL,
                                  related_name='medecinPatient')
    
