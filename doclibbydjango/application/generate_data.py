import random
import csv
from decimal import Decimal

# Generate 20 random data
data = []
for _ in range(20):
    entry = {
        'poids': Decimal(random.uniform(40, 150)),
        'tour_de_taille': random.randint(60, 120),
        'frequence_cardiaque': random.randint(60, 120),
        'tension_arterielle_systolique_matin': random.randint(100, 160),
        'tension_arterielle_systolique_soir': random.randint(100, 160),
        'tension_arterielle_diastolique_matin': random.randint(60, 100),
        'tension_arterielle_diastolique_soir': random.randint(60, 100),
        'symptomes_cardiovasculaires': 'Random symptoms description',
        'nombre_medicaments_jour': random.randint(0, 10),
        'oublie_medicament_matin': random.choice([True, False]),
        'oublie_medicament_soir': random.choice([True, False]),
        'effets_secondaires_remarques': random.choice([True, False]),
        'symptomes_particuliers_remarques': random.choice([True, False]),
        'effets_secondaires_description': 'Random effects description',
        'consommation_alcool': random.choice([True, False]),
        'grignotage_sucre': random.choice([True, False]),
        'grignotage_sale': random.choice([True, False]),
        'nombre_repas_jour': random.randint(1, 5),
        'quantite_eau_bue_litres': Decimal(random.uniform(0, 3)),
        'quantite_alcool_consomme_litres': Decimal(random.uniform(0, 2)),
        'activite_physique': random.choice([True, False]),
        'nature_activite_physique': 'Random activity description',
        'duree_activite_physique_minutes': random.randint(10, 120),
        'presence_dyspnee': random.choice([True, False]),
        'presence_oedeme': random.choice([True, False]),
        'presence_fievre': random.choice([True, False]),
        'presence_palpitation': random.choice([True, False]),
        'presence_douleur_thoracique': random.choice([True, False]),
        'presence_malaise': random.choice([True, False]),
        'heure_debut_palpitations': '10:00:00',
        'duree_total_palpitations_minutes': random.randint(5, 60),
        'heure_debut_douleurs_thoraciques': '12:00:00',
        'duree_total_douleurs_thoraciques_minutes': random.randint(5, 60),
        'heure_debut_malaises': '14:00:00',
        'duree_total_malaises_minutes': random.randint(5, 60),
        'natremie_mmol_per_l': Decimal(random.uniform(135, 145)),
        'potassium_mmol_per_l': Decimal(random.uniform(3.5, 5.5)),
        'creatinine_umol_per_l': Decimal(random.uniform(60, 120)),
        'clairance_creatinine_ml_per_min': Decimal(random.uniform(60, 120)),
        'nt_probnp_ng_per_l': Decimal(random.uniform(0, 500)),
        'fer_serique_mg_per_l': Decimal(random.uniform(50, 200)),
        'hemoglobine_g_per_100_ml': Decimal(random.uniform(10, 20)),
        'vitesse_sedimentation_mm': Decimal(random.uniform(1, 20)),
        'proteine_c_reactive_mg_per_l': Decimal(random.uniform(0, 10)),
        'troponine_jug_per_l': Decimal(random.uniform(0, 1)),
        'vitamine_d_ng_per_ml': Decimal(random.uniform(10, 80)),
        'acide_urique_mg_per_l': Decimal(random.uniform(2, 8)),
        'inr': Decimal(random.uniform(0.8, 2.5))
    }
    data.append(entry)
    
# Example to generate 10 random datas with np.random.choice: 'poids': Decimal(np.random.choice(np.arange(40, 150), 10))

# Save the data to a CSV file
csv_file = 'random_healthData.csv'
with open(csv_file, 'w', newline='') as file:
    fieldnames = data[0].keys()
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    for entry in data:
        writer.writerow(entry)

print(f'Data has been saved to {csv_file}')


from models import UserHealthData

def import_csv_data(csv_file):
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Create a UserHealthData instance for each row
            patient_data = UserHealthData(
                poids=row['poids'],
                tour_de_taille=row['tour_de_taille'],
                frequence_cardiaque=row['frequence_cardiaque'],
                # Set other fields similarly
            )
            patient_data.save()

if __name__ == '__main__':
    csv_file = 'random_healthData.csv'
    import_csv_data(csv_file)
