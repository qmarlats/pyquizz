"""
.. module:: menus
   :platform: Linux, Windows
   :synopsis: Allows users to choose what they want to do with menus

.. moduleauthor:: Quentin Marlats, Pierre Daudey, Louis Lhosmot, Maxime Cecchini, Benjamin Mitifiot, Charly Adam

"""

from pyquizz import settings
from game import play
from database.models import Category, Score

def main():
    """Main menu; allows to play game, show scores, show rules or leave game."""

    # Define user_input to enter the loop
    user_input = None

    print("Bonjour nous allons jouer ensemble a un blindtest.\nLe but du jeu sera sera de trouver le titre de la musique écoutée.\n")
    print("1 Jouer maintenant\n2 Voir les scores\n3 Règles du jeu\n4 Quitter\n")

    while user_input is None:
        user_input = input("Choisissez une option : ")
        try:
            user_input = int(user_input)
        except ValueError:
            print(settings.errors['NOT_A_NUMBER'])

        if user_input == 1:
            category()
        elif user_input == 2:
            show_scores()
        elif user_input == 3:
            show_rules()
        elif user_input == 4:
            exit()
        else:
            user_input = None
            print(settings.errors['CHOICE_NOT_EXISTS'])

def category():
    """Menu to choose the music gnere we want to listen to."""

    # Define user_input to enter the loop
    user_input = None

    # Get all categories in database
    categories = Category.select()

    # Show all categories available
    print("Styles de musique disponibles :")
    for category in categories:
        print("\t%i %s" % (category.id, category.name))

    while user_input is None:
        user_input = input("Choisisez maintenant votre style : ")
        try:
            user_input = int(user_input)
        except ValueError:
            print(settings.errors['NOT_A_NUMBER'])

        if user_input in range(1, len(categories) + 1):
            play.play(user_input)
        else:
            user_input = None
            print(settings.errors['CHOICE_NOT_EXISTS'])

def show_scores():
    """Display all scores of specified name"""

    user_input = None
    while user_input is None:
        user_input = input("Votre nom : ")
        if len(user_input) >= 1 and len(user_input) <= 30:
            scores = None

            try:
                scores = Score().select().where(name=user_input)
            except Exception:
                print("Impossible de récupérer les scores dans la base de données.")
                scores = Score().select().where(Score.name << [user_input])

            if scores is not None:
                for score in scores:
                    print("%s : %i" % (score.created_at.strftime("Le %d/%m/%Y à %H:%M:%S"), score.score))
            else:
                print("Aucun score ne correspond à votre recherche.")
        else:
            user_input = None
            print("Veuillez entrer un nom valide.")

def show_rules():
    """Diplay rules saved in "rules" file."""

    try:
        # Open file and close it even if an error occurs
        with open("%s/rules" % settings.STATIC_DIR, 'r') as f:
            rules = f.readlines()
            for i, rule in enumerate(rules):
                print("\n%s" % rule if i == 0 else rule)
    except IOError:
        print(settings.errors['CANT_OPEN_FILE'])
