import os

# Define paths
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
STATIC_DIR = os.path.join(BASE_DIR, 'static')
POPULATE_FILES_DIR = os.path.join(STATIC_DIR, 'populate')
MUSICS_DIR = os.path.join(STATIC_DIR, 'musics')

# Database settings
DB_NAME = "pyquizz"

# Define most used error messages
errors = {
    'NOT_A_NUMBER': "Veuillez entrer un nombre.",
    'CHOICE_NOT_EXISTS': "Ce choix n'existe pas.",
    'CANT_OPEN_FILE': "Impossible d'ouvrir le fichier."
}
