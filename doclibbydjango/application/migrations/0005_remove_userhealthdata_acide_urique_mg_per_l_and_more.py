# Generated by Django 4.2.5 on 2023-11-13 10:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0004_userhealthdata_date_remplissage_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userhealthdata',
            name='acide_urique_mg_per_l',
        ),
        migrations.RemoveField(
            model_name='userhealthdata',
            name='activite_physique',
        ),
        migrations.RemoveField(
            model_name='userhealthdata',
            name='clairance_creatinine_ml_per_min',
        ),
        migrations.RemoveField(
            model_name='userhealthdata',
            name='consommation_alcool',
        ),
        migrations.RemoveField(
            model_name='userhealthdata',
            name='creatinine_umol_per_l',
        ),
        migrations.RemoveField(
            model_name='userhealthdata',
            name='duree_activite_physique_minutes',
        ),
        migrations.RemoveField(
            model_name='userhealthdata',
            name='duree_total_douleurs_thoraciques_minutes',
        ),
        migrations.RemoveField(
            model_name='userhealthdata',
            name='duree_total_malaises_minutes',
        ),
        migrations.RemoveField(
            model_name='userhealthdata',
            name='duree_total_palpitations_minutes',
        ),
        migrations.RemoveField(
            model_name='userhealthdata',
            name='effets_secondaires_description',
        ),
        migrations.RemoveField(
            model_name='userhealthdata',
            name='effets_secondaires_remarques',
        ),
        migrations.RemoveField(
            model_name='userhealthdata',
            name='fer_serique_mg_per_l',
        ),
        migrations.RemoveField(
            model_name='userhealthdata',
            name='grignotage_sale',
        ),
        migrations.RemoveField(
            model_name='userhealthdata',
            name='grignotage_sucre',
        ),
        migrations.RemoveField(
            model_name='userhealthdata',
            name='hemoglobine_g_per_100_ml',
        ),
        migrations.RemoveField(
            model_name='userhealthdata',
            name='heure_debut_douleurs_thoraciques',
        ),
        migrations.RemoveField(
            model_name='userhealthdata',
            name='heure_debut_malaises',
        ),
        migrations.RemoveField(
            model_name='userhealthdata',
            name='heure_debut_palpitations',
        ),
        migrations.RemoveField(
            model_name='userhealthdata',
            name='inr',
        ),
        migrations.RemoveField(
            model_name='userhealthdata',
            name='natremie_mmol_per_l',
        ),
        migrations.RemoveField(
            model_name='userhealthdata',
            name='nature_activite_physique',
        ),
        migrations.RemoveField(
            model_name='userhealthdata',
            name='nombre_medicaments_jour',
        ),
        migrations.RemoveField(
            model_name='userhealthdata',
            name='nombre_repas_jour',
        ),
        migrations.RemoveField(
            model_name='userhealthdata',
            name='nt_probnp_ng_per_l',
        ),
        migrations.RemoveField(
            model_name='userhealthdata',
            name='oublie_medicament_matin',
        ),
        migrations.RemoveField(
            model_name='userhealthdata',
            name='oublie_medicament_soir',
        ),
        migrations.RemoveField(
            model_name='userhealthdata',
            name='potassium_mmol_per_l',
        ),
        migrations.RemoveField(
            model_name='userhealthdata',
            name='presence_douleur_thoracique',
        ),
        migrations.RemoveField(
            model_name='userhealthdata',
            name='presence_dyspnee',
        ),
        migrations.RemoveField(
            model_name='userhealthdata',
            name='presence_fievre',
        ),
        migrations.RemoveField(
            model_name='userhealthdata',
            name='presence_malaise',
        ),
        migrations.RemoveField(
            model_name='userhealthdata',
            name='presence_oedeme',
        ),
        migrations.RemoveField(
            model_name='userhealthdata',
            name='presence_palpitation',
        ),
        migrations.RemoveField(
            model_name='userhealthdata',
            name='proteine_c_reactive_mg_per_l',
        ),
        migrations.RemoveField(
            model_name='userhealthdata',
            name='quantite_alcool_consomme_litres',
        ),
        migrations.RemoveField(
            model_name='userhealthdata',
            name='quantite_eau_bue_litres',
        ),
        migrations.RemoveField(
            model_name='userhealthdata',
            name='symptomes_particuliers_remarques',
        ),
        migrations.RemoveField(
            model_name='userhealthdata',
            name='troponine_jug_per_l',
        ),
        migrations.RemoveField(
            model_name='userhealthdata',
            name='vitamine_d_ng_per_ml',
        ),
        migrations.RemoveField(
            model_name='userhealthdata',
            name='vitesse_sedimentation_mm',
        ),
    ]
