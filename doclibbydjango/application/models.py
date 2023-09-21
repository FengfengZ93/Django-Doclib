from django.db import models

class UserHealthData(models.Model):
    # Poids
    poids = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, help_text="Indiquez votre poids")
    
    # Tour de taille en cm
    tour_de_taille = models.PositiveIntegerField(blank=True, null=True, help_text="Indiquez votre tour de taille en cm")
    
    # Informations cardiaques et tension artérielle
    frequence_cardiaque = models.PositiveIntegerField(blank=True, null=True, help_text="Indiquez votre fréquence cardiaque par minute")
    tension_arterielle_systolique_matin = models.PositiveIntegerField(blank=True, null=True, help_text="Indiquez votre Tension artérielle systolique (prise du matin)")
    tension_arterielle_systolique_soir = models.PositiveIntegerField(blank=True, null=True, help_text="Indiquez votre Tension artérielle systolique (prise du soir)")
    tension_arterielle_diastolique_matin = models.PositiveIntegerField(blank=True, null=True, help_text="Indiquez votre Tension artérielle diastolique (prise du matin)")
    tension_arterielle_diastolique_soir = models.PositiveIntegerField(blank=True, null=True, help_text="Indiquez votre Tension artérielle diastolique (prise du soir)")
    symptomes_cardiovasculaires = models.TextField(blank=True, null=True, help_text="Décrivez vos symptômes cardiovasculaires en quelques mots")
    
    # Prise de médicaments
    nombre_medicaments_jour = models.PositiveIntegerField(blank=True, null=True, help_text="Indiquez le nombre de médicaments pris dans la journée")
    oublie_medicament_matin = models.BooleanField(default=False, help_text="Oublie de prendre le(s) médicament(s) le matin")
    oublie_medicament_soir = models.BooleanField(default=False, help_text="Oublie de prendre le(s) médicament(s) le soir")
    effets_secondaires_remarques = models.BooleanField(default=False, help_text="Effet(s) secondaire(s) remarqué(s)")
    symptomes_particuliers_remarques = models.BooleanField(default=False, help_text="Symptôme(s) particulier(s) remarqué(s)")
    effets_secondaires_description = models.TextField(blank=True, null=True, help_text="Décrivez vos effets secondaires et/ou symptômes particuliers remarqués en quelques mots")
    
    # Alimentation
    consommation_alcool = models.BooleanField(default=False, help_text="Consommation d'alcool")
    grignotage_sucre = models.BooleanField(default=False, help_text="Grignotage sucré")
    grignotage_sale = models.BooleanField(default=False, help_text="Grignotage salé")
    nombre_repas_jour = models.PositiveIntegerField(blank=True, null=True, help_text="Indiquez le nombre de repas pris durant la journée")
    quantite_eau_bue_litres = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, help_text="Indiquez la quantité d'eau bu aujourd'hui")
    quantite_alcool_consomme_litres = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, help_text="Indiquez la quantité d'alcool bu aujourd'hui")
    
    # Activité physique
    activite_physique = models.BooleanField(default=False, help_text="J'ai eu une activité physique aujourd'hui")
    nature_activite_physique = models.CharField(max_length=200, blank=True, null=True, help_text="Décrivez la nature de votre activité physique")
    duree_activite_physique_minutes = models.PositiveIntegerField(blank=True, null=True, help_text="Indiquez la durée de votre activité physique en minutes")
    
    # Autres symptômes
    presence_dyspnee = models.BooleanField(default=False, help_text="Présence de dyspnée")
    presence_oedeme = models.BooleanField(default=False, help_text="Présence d'œdème")
    presence_fievre = models.BooleanField(default=False, help_text="Présence de fièvre")
    presence_palpitation = models.BooleanField(default=False, help_text="Présence de palpitation")
    presence_douleur_thoracique = models.BooleanField(default=False, help_text="Présence de douleur thoracique")
    presence_malaise = models.BooleanField(default=False, help_text="Présence de malaise")
    heure_debut_palpitations = models.TimeField(blank=True, null=True, help_text="Indiquez l'heure de début des palpitations")
    duree_total_palpitations_minutes = models.PositiveIntegerField(blank=True, null=True, help_text="Indiquez la durée totale des palpitations apparues durant la journée en minutes")
    heure_debut_douleurs_thoraciques = models.TimeField(blank=True, null=True, help_text="Indiquez l'heure de début des douleurs thoraciques")
    duree_total_douleurs_thoraciques_minutes = models.PositiveIntegerField(blank=True, null=True, help_text="Indiquez la durée totale des douleurs thoraciques apparues durant la journée en minutes")
    heure_debut_malaises = models.TimeField(blank=True, null=True, help_text="Indiquez l'heure de début des malaises")
    duree_total_malaises_minutes = models.PositiveIntegerField(blank=True, null=True, help_text="Indiquez la durée totale des malaises apparus durant la journée en minutes")
    
    # Autres informations médicales
    natremie_mmol_per_l = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True, help_text="Indiquez vos valeurs de natremie en mmol/l (millimoles par litre)")
    potassium_mmol_per_l = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True, help_text="Indiquez vos valeurs de potassium en mmol/l (millimoles par litre)")
    creatinine_umol_per_l = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True, help_text="Indiquez vos valeurs de créatinine en umol/l (micromoles per litre)")
    clairance_creatinine_ml_per_min = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True, help_text="Indiquez vos valeurs de clairance de créatinine en ml/min (millilitres per minute)")
    nt_probnp_ng_per_l = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True, help_text="Indiquez votre taux de NT Probnp en ng/l (nanogrammes par litre)")
    fer_serique_mg_per_l = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True, help_text="Indiquez votre taux de fer sérique mg/l (milligrame par litre)")
    hemoglobine_g_per_100_ml = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True, help_text="Indiquez votre taux d'hémoglobine en g/100 ml (gramme par 100 millilitre)")
    vitesse_sedimentation_mm = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True, help_text="Indiquez vos valeurs de Vitesse de sédimentation (VS) en milimètre")
    proteine_c_reactive_mg_per_l = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True, help_text="Indiquez votre taux protéine C réactive en mg/l")
    troponine_jug_per_l = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True, help_text="Indiquez votre taux de troponine en jug/l (microgrammes par litre)")
    vitamine_d_ng_per_ml = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True, help_text="Indiquez votre taux de vitamine D en ng/ml de sang")
    acide_urique_mg_per_l = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True, help_text="Indiquez votre taux d'acide urique en mg/l")
    inr = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True, help_text="Indiquez votre taux de INR (International Normalized Ratio)")

    def __str__(self):
        return f"Health Data for User ID: {self.pk}"
    


# class StressEvaluation(models.Model):
#     user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='stress_evaluations', help_text="User who completed the evaluation")
#     evaluation_date = models.DateField(auto_now_add=True, help_text="Date of the evaluation")
    
#     # Symptom scores (Irritability to Total Stress Impact)
#     SCORE_CHOICES = (
#         (0, '0'),
#         (1, '1'),
#         (5, '5'),
#         (10, '10'),
#     )
    
#     irritability = models.PositiveIntegerField(default=0, choices=SCORE_CHOICES, help_text="Irritability score (0, 1, 5, 10)")
#     feelings_of_depression = models.PositiveIntegerField(default=0, choices=SCORE_CHOICES, help_text="Feelings of depression score (0, 1, 5, 10)")
#     dry_mouth_or_sore_throat = models.PositiveIntegerField(default=0, choices=SCORE_CHOICES, help_text="Dry mouth or sore throat score (0, 1, 5, 10)")
#     impulsive_actions_or_gestures = models.PositiveIntegerField(default=0, choices=SCORE_CHOICES, help_text="Impulsive actions or gestures score (0, 1, 5, 10)")
#     teeth_grinding = models.PositiveIntegerField(default=0, choices=SCORE_CHOICES, help_text="Teeth grinding score (0, 1, 5, 10)")
#     difficulty_staying_seated = models.PositiveIntegerField(default=0, choices=SCORE_CHOICES, help_text="Difficulty staying seated score (0, 1, 5, 10)")
#     nightmares = models.PositiveIntegerField(default=0, choices=SCORE_CHOICES, help_text="Nightmares score (0, 1, 5, 10)")
#     diarrhea = models.PositiveIntegerField(default=0, choices=SCORE_CHOICES, help_text="Diarrhea score (0, 1, 5, 10)")
#     verbal_attacks_on_others = models.PositiveIntegerField(default=0, choices=SCORE_CHOICES, help_text="Verbal attacks on others score (0, 1, 5, 10)")
#     emotional_ups_and_downs = models.PositiveIntegerField(default=0, choices=SCORE_CHOICES, help_text="Emotional ups and downs score (0, 1, 5, 10)")
#     strong_desire_to_cry = models.PositiveIntegerField(default=0, choices=SCORE_CHOICES, help_text="Strong desire to cry score (0, 1, 5, 10)")
#     strong_desire_to_flee = models.PositiveIntegerField(default=0, choices=SCORE_CHOICES, help_text="Strong desire to flee score (0, 1, 5, 10)")
#     strong_desire_to_harm = models.PositiveIntegerField(default=0, choices=SCORE_CHOICES, help_text="Strong desire to harm score (0, 1, 5, 10)")
#     confused_thoughts = models.PositiveIntegerField(default=0, choices=SCORE_CHOICES, help_text="Confused thoughts score (0, 1, 5, 10)")
#     faster_pace_of_thoughts = models.PositiveIntegerField(default=0, choices=SCORE_CHOICES, help_text="Faster pace of thoughts score (0, 1, 5, 10)")
#     generalized_fatigue_or_heaviness = models.PositiveIntegerField(default=0, choices=SCORE_CHOICES, help_text="Generalized fatigue or heaviness score (0, 1, 5, 10)")
#     feeling_overloaded = models.PositiveIntegerField(default=0, choices=SCORE_CHOICES, help_text="Feeling overloaded score (0, 1, 5, 10)")
#     feeling_emotionally_fragile = models.PositiveIntegerField(default=0, choices=SCORE_CHOICES, help_text="Feeling emotionally fragile score (0, 1, 5, 10)")
#     feeling_sad = models.PositiveIntegerField(default=0, choices=SCORE_CHOICES, help_text="Feeling sad score (0, 1, 5, 10)")
#     feeling_anxious = models.PositiveIntegerField(default=0, choices=SCORE_CHOICES, help_text="Feeling anxious score (0, 1, 5, 10)")
#     emotional_tension = models.PositiveIntegerField(default=0, choices=SCORE_CHOICES, help_text="Emotional tension score (0, 1, 5, 10)")
#     hostility_towards_others = models.PositiveIntegerField(default=0, choices=SCORE_CHOICES, help_text="Hostility towards others score (0, 1, 5, 10)")
#     tremors_or_nervous_gestures = models.PositiveIntegerField(default=0, choices=SCORE_CHOICES, help_text="Tremors or nervous gestures score (0, 1, 5, 10)")
#     stuttering_or_verbal_hesitation = models.PositiveIntegerField(default=0, choices=SCORE_CHOICES, help_text="Stuttering or verbal hesitation score (0, 1, 5, 10)")
#     difficulty_concentrating = models.PositiveIntegerField(default=0, choices=SCORE_CHOICES, help_text="Difficulty concentrating score (0, 1, 5, 10)")
#     difficulty_organizing_thoughts = models.PositiveIntegerField(default=0, choices=SCORE_CHOICES, help_text="Difficulty organizing thoughts score (0, 1, 5, 10)")
#     difficulty_sleeping_through_the_night = models.PositiveIntegerField(default=0, choices=SCORE_CHOICES, help_text="Difficulty sleeping through the night score (0, 1, 5, 10)")
#     frequent_urination = models.PositiveIntegerField(default=0, choices=SCORE_CHOICES, help_text="Frequent urination score (0, 1, 5, 10)")
#     stomach_pains_or_digestive_issues = models.PositiveIntegerField(default=0, choices=SCORE_CHOICES, help_text="Stomach pains or digestive issues score (0, 1, 5, 10)")
#     impatience = models.PositiveIntegerField(default=0, choices=SCORE_CHOICES, help_text="Impatience score (0, 1, 5, 10)")
#     headaches = models.PositiveIntegerField(default=0, choices=SCORE_CHOICES, help_text="Headaches score (0, 1, 5, 10)")
#     back_or_neck_pain = models.PositiveIntegerField(default=0, choices=SCORE_CHOICES, help_text="Back or neck pain score (0, 1, 5, 10)")
#     appetite_loss_or_gain = models.PositiveIntegerField(default=0, choices=SCORE_CHOICES, help_text="Appetite loss or gain score (0, 1, 5, 10)")
#     loss_of_interest_in_sex = models.PositiveIntegerField(default=0, choices=SCORE_CHOICES, help_text="Loss of interest in sex score (0, 1, 5, 10)")
#     frequent_forgetfulness = models.PositiveIntegerField(default=0, choices=SCORE_CHOICES, help_text="Frequent forgetfulness score (0, 1, 5, 10)")
#     chest_pains_or_tightness = models.PositiveIntegerField(default=0, choices=SCORE_CHOICES, help_text="Chest pains or tightness score (0, 1, 5, 10)")
#     significant_conflicts_with_others = models.PositiveIntegerField(default=0, choices=SCORE_CHOICES, help_text="Significant conflicts with others score (0, 1, 5, 10)")
#     difficulty_getting_up_after_sleep = models.PositiveIntegerField(default=0, choices=SCORE_CHOICES, help_text="Difficulty getting up after sleep score (0, 1, 5, 10)")
#     feeling_that_things_are_out_of_control = models.PositiveIntegerField(default=0, choices=SCORE_CHOICES, help_text="Feeling that things are out of control score (0, 1, 5, 10)")
#     difficulty_sustaining_a_long_continuous_activity = models.PositiveIntegerField(default=0, choices=SCORE_CHOICES, help_text="Difficulty sustaining a long continuous activity score (0, 1, 5, 10)")
#     withdrawal_or_isolation = models.PositiveIntegerField(default=0, choices=SCORE_CHOICES, help_text="Withdrawal or isolation score (0, 1, 5, 10)")
#     difficulty_falling_asleep = models.PositiveIntegerField(default=0, choices=SCORE_CHOICES, help_text="Difficulty falling asleep score (0, 1, 5, 10)")
#     difficulty_recovering_from_a_disturbing_event = models.PositiveIntegerField(default=0, choices=SCORE_CHOICES, help_text="Difficulty recovering from a disturbing event score (0, 1, 5, 10)")
#     sweaty_palms = models.PositiveIntegerField(default=0, choices=SCORE_CHOICES, help_text="Sweaty palms score (0, 1, 5, 10)")
    
#     # Total Stress Impact
#     total_stress_impact = models.PositiveIntegerField(default=0, help_text="Total impact of stress in your current life")

#     def __str__(self):
#         return f"Stress Evaluation for User ID: {self.user_id} on {self.evaluation_date}"
