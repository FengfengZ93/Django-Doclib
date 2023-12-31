"""
URL configuration for doclibbydjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from application.views import accueil, comptes, edaia, associationMedecinPatient, UserHealthData, StressEvaluation, historique
from authentification.views import connexion, deconnexion, CreatPatient 

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accueil", accueil, name="accueil"),
    path("", connexion, name="connexion"),
    path("comptes", comptes, name="comptes"),
    path("edaia", edaia, name="edaia"),
    path("UserHealthData", UserHealthData, name="UserHealthData"),
    path('StressEvaluation', StressEvaluation, name='StressEvaluation'),
    path("associationMedecinPatient", associationMedecinPatient, name="associationMedecinPatient"),
    path("deconnexion", deconnexion, name="deconnexion"),
    path("CreatPatient", CreatPatient, name="CreatPatient"),
    path("historique", historique, name="historique",)
]
