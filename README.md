# Django-Doclib
Project Django-doctor lib

## Overview
This application is a Django-based web platform designed for health management, allowing tracking of user health data and stress evaluations. It features two main components: a health data management system (`application`) and a user authentication system (`authentification`).

## Features
- User health data tracking and management.
- Stress evaluation recording and analysis.
- User roles including patients, doctors, and administrators.
- Customized user authentication and management.

## Diagram of structure

![Diagram of structure](Django_Doclib.png)

<img src="Django_Doclib.png" alt="Diagram of structure" title="Optional title">

## Data (database schema)
![authentification_utilisateur](\Formation IA\Django-Doclib\authentification_utilisateur.png)


## Installation
To set up the project, follow these steps:

1. Clone the repository:
git clone <git@github.com:FengfengZ93/Django-Doclib.git>

2. Install required dependencies:
pip install -r requirements.txt

3. Run migrations to create database schema:
python manage.py makemigrations
python manage.py migrate

4. Create a superuser account:
python manage.py createsuperuser

5. Run the development server:
python manage.py runserver

6. Access the application at `http://127.0.0.1:8000/`.

## Application Structure

### `application` App
- **Models**: `UserHealthData`, `StressEvaluation`
- **Forms**: `UserHealthDataForm`, `StressEvaluationForm`
- **Admin**: Custom admin configurations for models.
- **Views**: Functions for different user interfaces and interactions.

### `authentification` App
- **Models**: `Utilisateur`, `medecinPatient`
- **Admin**: Custom admin configurations for the `Utilisateur` model.
- **Views**: Login, logout, user creation, and initial data population functions.

## Usage
- Users can log in, view, and manage their health data.
- Stress evaluations can be recorded and tracked over time.
- Administrators can manage user accounts and view data in the Django Admin panel.


## License
[MIT License](LICENSE)

