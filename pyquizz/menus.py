from database import models
import play

def main_menu():
    print("Bonjour nous allons jouer ensemble a un blindtest.\nLe but du jeu sera sera de trouver le titre de la musique écoutée.\n")
    print("1 Jouer maintenant\n2 Voir les scores\n3 Règles du jeu\n4 Quiter\n")

    menu_input = 0

    while menu_input !=1 and menu_input !=2 and menu_input != 4:
        menu_input = input("Choisissez une option : ")

        try:
            menu_input = int(menu_input)
        except ValueError:
            menu_input = 0
            print("Veuillez entrer un nombre.")

        if menu_input == 1:
            category_menu()
        elif menu_input == 2:
            print("Pas encore regardable")
        elif menu_input == 3:
            show_rules()
        elif menu_input == 4:
            exit()
        else:
            print("Ce choix n'existe pas.")

def category_menu():
    print("Styles de musique disponibles :")
    categories = models.Category.select()
    for category in categories:
        print("\t%s" % category.name)

    category_input = 0

    while category_input < 1 or category_input > len(categories):
        category_input = input("Choisisez maintenant votre style : ")

        try:
            category_input = int(category_input)
        except ValueError:
            category_input = 0
            print("Veuillez entrer un nombre.")

        if category_input >= 1 and category_input <= 7:
            play.play(category_input)
        else:
            print("Ce choix n'existe pas.")

def show_rules():
    rules = open('rules', 'r').readlines()
    for i, rule in enumerate(rules):
        print("\n%s" % rule if i == 0 else rule)
