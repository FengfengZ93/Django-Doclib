from django import forms
from .models import UserHealthData, StressEvaluation

# class FUserHealthDatareationForm(forms.ModelForm):
#     class Meta:
#         model = UserHealthData
#         fields = 'all'


class UserHealthDataForm(forms.ModelForm):
    class Meta:
        model = UserHealthData
        fields = "__all__"
"""
class InfoGeneraleForm(forms.ModelForm):
    class Meta:
        model = UserHealthData
        fields = ("patient", 
                  'date_remplissage', 
                  'periodicite_jours',
                  'is_late',
                  "poids",
                  "tour_de_taille_cm",)
    
class EtatDeSanteForm(forms.ModelForm):
    class Meta:
        model = UserHealthData
        fields = ("frequence_cardiaque_min", 
                  'tension_arterielle_systolique_matin', 
                  'tension_arterielle_systolique_soir',
                  'tension_arterielle_diastolique_matin',
                  "tension_arterielle_diastolique_soir",
                  "symptomes_cardiovasculaires",
                  "nb_medicaments_jour",)
"""
class StressEvaluationForm(forms.ModelForm):
    class Meta:
        model = StressEvaluation
        fields = "__all__"