from django.shortcuts import render
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import redirect
from authentification.models import Utilisateur
import random 
import string
import pandas as pd

def connexion(request):
    message = ""
    # A t'on reçu des datas d'un formulaire ? Si oui la condition est True
    if request.method == "POST": 
        username = request.POST["username"]
        motDePasse = request.POST["motDePasse"]
        verification = authenticate(username = username,
                                    password = motDePasse)
        if verification != None:
            login(request, verification)
            return redirect("accueil")
        else:
            message = "username or password is wrong"
    
    return render(request,
                      "connexion.html", {"message" : message})

def deconnexion(request):
    logout(request)
    return redirect("connexion")


def inscription(request):
    ideeMDP = "".join([random.choice(string.printable) for _ in range(12)]).replace(" ", "")
    if request.method == "POST": 
        username = request.POST["username"]
        motDePasse = request.POST["motDePasse"]
        nouveauCompte = Utilisateur.objects.create_user(username = username,
                                    password = motDePasse)
        
        return redirect("connexion")
    
    return render(request,
                      "inscription.html", {"ideeMDP" : ideeMDP.replace(" ", "")})



def alimentationPatients():
    name = "P"
    number = 1000
    listePatients = [name+str(number+i) for i in range(20)]
    for patient in listePatients:
        Utilisateur.objects.create_user(username = patient,
                                    password = patient,
                                    role="patient")
    # OLD
    #listePatients = pd.read_csv("listePatients.csv")
    #for index, valeurs in listePatients.iterrows():
        #champDBB = Utilisateur._meta.get_fields()
        
        #Utilisateur.objects.create_user(username = valeurs.username,
        #                                password = valeurs.motDePasse,
        #                                role="patient")
def alimentationMedecin():
    name = "M"
    number = 1000
    listeMedecins = [name+str(number+i) for i in range(20)]
    for medecin in listeMedecins:
        Utilisateur.objects.create_user(username = medecin,
                                    password = medecin,
                                    role="medecin")
    # OLD
    #listeMedecins = pd.read_csv("listeMedecins.csv")
    #for index, valeurs in listeMedecins.iterrows():
    #    Utilisateur.objects.create_user(username = valeurs.username,
    #                                    password = valeurs.motDePasse,
    #                                    role="medecin")
      
if len(Utilisateur.objects.filter(role="patient")) == 0:
    alimentationPatients()
if len(Utilisateur.objects.filter(role="medecin")) == 0:
    alimentationMedecin() 