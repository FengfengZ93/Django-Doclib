from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from authentification.models import Utilisateur, medecinPatient
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from application.models import UserHealthData

from application.forms import UserHealthDataForm, StressEvaluationForm
import os
from django.http import HttpResponse
import datetime


@login_required
def accueil(request):
    prenom = request.user.username
    return render(request,"accueil.html",
                  context={"prenom": prenom})

# @login_required
# def accueil(request):
#     utilisateur = Utilisateur.objects.get(username=request.user.username)

#     # Check if it's the user's first login
#     if utilisateur.first_login:
#         # Redirect to change password page
#         return redirect('change_password')

#     prenom = request.user.username
#     return render(request,"accueil.html",
#                   context={"prenom": prenom})

# @login_required
# def change_password(request):
#     if request.method == 'POST':
#         form = PasswordChangeForm(request.user, request.POST)
#         if form.is_valid():
#             user = form.save()
#             user.first_login = False  # Set first_login to False after password change
#             user.save()
#             update_session_auth_hash(request, user)  # Important!
#             return redirect('accueil')
#         else:
#             # Handle invalid form
#             pass
#     else:
#         form = PasswordChangeForm(request.user)
#     return render(request, 'change_password.html', {'form': form})


@login_required
def comptes(request):
    regexMDP = "^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#$%^&*()_+-]).{8,}$"
    message = ""
    if request.method == "POST":
        ancienMDP = request.POST["ancienMDP"]
        nouveauMDP1 = request.POST["nouveauMDP1"]
        nouveauMDP2 = request.POST["nouveauMDP2"]
        
        verification = authenticate(username = request.user.username,
                                    password = ancienMDP)
        if verification != None:
            if nouveauMDP1 == nouveauMDP2:
                utilisateur = Utilisateur.objects.get(username = request.user.username)
                #utilisateur = Utilisateur.objects.get(id=request.user.id)
                utilisateur.set_password(request.POST.get("nouveauMDP1"))
                utilisateur.save()
                return redirect("accueil")
            else:
                message = "⚠️ Les deux mot de passe ne concordent pas ⚠️"
        else:
            message = "L'ancien mot de passe n'est pas bon. T'es qui toi ? 😡"
    return render(request,
                  "comptes.html",
                  {"regexMDP" : regexMDP, "message" : message})

@login_required
def edaia(request):
    if request.user.role != "medecin":
        return redirect("https://media.tenor.com/2euSOQYdz8oAAAAj/this-was-technically-illegal-maclen-stanley.gif")
    else:
        return render(request, "edaia.html")

@login_required
def historique(request):
    """
     # Je récupère les champs de la table formulaire santé
    champsFormulaireSante = [field.name for field in UserHealthData._meta.get_fields()]
    # Je récupère les ids des lignes de la table formulaire santé
    idDesFormulaires = [valeur.id for valeur in UserHealthData.objects.all()]
    # Je crée une liste qui contiendra les valeurs des lignes
    # Il y a autant d'élément que de ligne, donc que d'ids récupéré
    # FormulaireSante.objects.filter(id=id).values()[0].values()
    # Dans le code ci-dessus je récupère la ligne ayant un certain id
    # Ensuite je récupère les valeurs de la ligne .values
    # Le 1er élément qui est le dictionnaire des colonnes/valeurs
    # et enfin uniquement les valeurs
    
    #dataFormulaireSante = [FormulaireSante.objects.filter(id=id).values()[0].values() for id in idDesFormulaires]
    # On créé une liste des données du formulaires de santé général
    dataFormulaireSante = []
    # On boucle dans les lignes du formulairs > ligne 1, 2, 3...
    for id in idDesFormulaires:
        # On récupère sous forme de liste l'ensemble de la ligne ayant un id donnée
        info = list(UserHealthData.objects.filter(id=id).values()[0].values())
        # On récupère l'username en nous basant sur la colonne de l'id dans la table du formulaire
        # On écrase l'ensemble valeur parce qu'on veut pas l'ID mais le username
        info[1] = Utilisateur.objects.filter(id=info[1])[0].username
        # On ajoute la ligne complète dans la liste dataFormulaireSante
        dataFormulaireSante.append(info)

    # Je récupère les objets patients du médecin connecté
    patientsDuMedecin = [patients for patients in medecinPatient.objects.filter(idMedecin=Utilisateur.objects.filter(username=request.user.username)[0])]
    # Je récupère les IDs des patients du médecin
    idPatientsDuMedecin = [Utilisateur.objects.filter(username=patient.idPatient)[0].id for patient in patientsDuMedecin]
    dataFormulaireSanteMedecinPatients = []

    # On boucle dans les lignes du formulairs > ligne 1, 2, 3...
    for patient in idPatientsDuMedecin:
        
        # On récupère sous forme de liste l'ensemble de la ligne ayant un id donnée
        info = list(UserHealthData.objects.filter(patient=patient).values()[0].values())
        # On récupère l'username en nous basant sur la colonne de l'id dans la table du formulaire
        # On écrase l'ensemble valeur parce qu'on veut pas l'ID mais le username
        info[1] = Utilisateur.objects.filter(id=info[1])[0].username
        # On ajoute la ligne complète dans la liste dataFormulaireSante
        dataFormulaireSanteMedecinPatients.append(info)

    print("DDDDDDDD :", dataFormulaireSante)
    return render(request, "historique.html",
                   {"dataFormulaireSante" : dataFormulaireSante,
                   "champsFormulaireSante" : "22222222",
                   "patientsDuMedecin" : patientsDuMedecin,
                   "dataFormulaireSanteMedecinPatients" : dataFormulaireSanteMedecinPatients})

    """
    # print(":", UserHealthData.objects.all() )
    return redirect("https://media.tenor.com/qTOYKUNpqPQAAAAC/skeleton-waiting-skeleton.gif")


@login_required
def associationMedecinPatient(request):
    # 1- Récupérer la liste des id des médecins et des patients
    # 2- Ensuite on ne garde que les patients qui ne sont pas dans la table medecinPatient
    # 3- On créé ensuite un template qui contiendra une liste déroulante
    # 4- Dans cette liste déroulante on va afficher d'un côté les médecins
    # et de l'autre les patients filtrés (voir étapge 2)
    # https://developer.mozilla.org/fr/docs/Web/HTML/Element/select
    
    medecins = [medecin for medecin in Utilisateur.objects.filter(role="medecin")]
    patients = [patient for patient in Utilisateur.objects.filter(role="patient")]
    listePatientsAssocies = [ligne.idPatient for ligne in medecinPatient.objects.all()]
    print("listePatientsAssocies :", listePatientsAssocies)
    listePatientsNonAssocies = [patient for patient in patients if patient not in listePatientsAssocies]
    tableAssociationMedecinPatient = medecinPatient.objects.all()
    
    if request.method == "POST":
        medecin = request.POST["medecin"]
        patient = request.POST["patient"]
        print("medecin", type(medecin), medecin)
        medecinPatient(idMedecin = Utilisateur.objects.filter(username=medecin)[0], 
                       idPatient = Utilisateur.objects.filter(username=patient)[0]).save()
        return redirect("associationMedecinPatient")
    return render(request, "associationMedecinPatient.html",
                  {"listePatientsNonAssocies" : listePatientsNonAssocies,
                   "medecins" : medecins,
                   "tableAssociationMedecinPatient" : tableAssociationMedecinPatient})

@login_required
def UserHealthData(request):
    if request.method == "POST":
       formulaire = UserHealthDataForm(request.POST)
       if formulaire.is_valid():
           sauvagarde = formulaire.save() 
    else:
        formulaire = UserHealthDataForm()
    return render(request,
                  "UserHealthData.html",
                  {"formulaire" : formulaire})

@login_required
def StressEvaluation(request):
    if request.method == "POST":
       formulaire = StressEvaluationForm(request.POST)
       if formulaire.is_valid():
           sauvagarde = formulaire.save() 
    else:
        formulaire = StressEvaluationForm()
    return render(request,
                  "StressEvaluation.html",
                  {"formulaire" : formulaire})
