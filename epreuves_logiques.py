from fonctions_utiles import verification_saisie_entier
from random import randint




def suiv(joueur):
    """int -> int
    Renvoie le joueur suivant
    """
    return 1 if joueur == 0 else 0

def grille_vide():
    """None -> Table[[string, string, string], [string, string, string], [string, string, string]]
    initialise une grille vide
    """
    return [[" " for _ in range(3)] for _ in range(3)]

def affiche_grille(grille, message):
    """Table[[string, string, string], [string, string, string], [string, string, string]], string -> None
    Affich la grille avec un message
    """
    print(message)
    for ligne in grille:
        print("|", end="")
        for cellule in ligne:
            print(cellule, end="|")
        print()
    print("-------")


def demande_position():
    """ None -> tuple[int, int]
    Demande au joueur de saisir une position (x, y)
    """
    while True:
        x = input("Entrez la position (ligne) 1 et 3 : ")
        y = input("Entrez la position (colonne) entre 1 et 3 : ")
        if verification_saisie_entier(x) and verification_saisie_entier(y):
            x, y = int(x) - 1, int(y) - 1
            if 0 <= x < 3 and 0 <= y < 3 :
                return x, y
        print("Coordonnées invalides. Veuillez réessayer.")

def init():
    """ None -> Table[[string, string, string], [string, string, string], [string, string, string]]
    permet d'initailiser la grille de jeu
    """
    grille = grille_vide()
    print("Positionnez vos bateaux :")
    for i in range(1,3):
        print(f"Bateau {i}")
        x, y = demande_position()
        while not grille[x][y] == " ":
            print("position déja occupé")
            x, y = demande_position()
        grille[x][y] = 'B'
    return grille

def init_bot():
    """ None -> Table[[string, string, string], [string, string, string], [string, string, string]]
    permet d'initailiser la grille de jeu pour un bot
    """
    grille = grille_vide()
    for i in range(1, 3):
        x, y = randint(0, 2), randint(0, 2)
        while not grille[x][y] == " ":
            x, y = randint(0, 2), randint(0, 2)
        grille[x][y] = 'B'
    return grille





def tour(joueur, grille_tirs_joueurs, grille_adversaires):
    """int, Table[[string, string, string], [string, string, string], [string, string, string]],
       Table[[string, string, string], [string, string, string], [string, string, string]] -> None
    Permet à un joueur de jouer un tour
    """
    if joueur == 0:
        print("C'est a votre tour de faire feu !: ")
        affiche_grille(grille_tirs_joueurs, "Rappel de l'historique des tirs que vous avez effectués")
        x, y = demande_position()
        while grille_tirs_joueurs[x][y] == "X" or grille_tirs_joueurs[x][y] == "·":
            x, y = demande_position()
        if grille_adversaires[x][y] == "B":
            grille_tirs_joueurs[x][y] = "X"
            print("Touché coulé !")
        else:
            print("Dans l'eau...")
            grille_tirs_joueurs[x][y] = "·"
    else:
        x, y = randint(0, 2), randint(0, 2)
        while grille_tirs_joueurs[x][y] == "X" or grille_tirs_joueurs[x][y] == "·":
            x, y = randint(0, 2), randint(0, 2)
        print(f"Le maître du jeu a tiré en position {x + 1 ,y + 1}")
        if grille_adversaires[x][y] == "B":
            print("Touché coulé !")
            grille_tirs_joueurs[x][y] = "X"
        else:
            print("Dans l'eau...")
            grille_tirs_joueurs[x][y] = "·"
    print()

def gagne(grille_tirs_joueurs):
    """Table[[string, string, string], [string, string, string], [string, string, string]] -> bool
    retourne si la grille du joueur est gagnante"""
    cpt = 0
    for elm in grille_tirs_joueurs:
        for elm2 in elm:
            if elm2 == 'X':
                cpt += 1
    return cpt == 2

def jeu_bataille_naval():
    """ None -> None
    Déroulement du jeu de bataille navale
    """
    print("Chaque joueur doit placer 2 bateaux sur une grille de 3x3.")
    print("Les bateaux sont représentés par 'B' et les tirs manqués par '.'. \nLes bateaux coulés sont marqués par 'x'.")
    grille_joueurs = init()
    grille_tirs_joueurs = grille_vide()
    grille_tirs_maitre =grille_vide()
    grille_maitre = init_bot()
    joueur = 0
    while not gagne(grille_tirs_joueurs) and not gagne(grille_tirs_maitre):
        if joueur == 0:
            tour(joueur, grille_tirs_joueurs, grille_maitre)
        else:
            tour(joueur, grille_tirs_maitre, grille_joueurs)
        joueur = suiv(joueur)
    if gagne(grille_tirs_joueurs):
        print("Vous avez gagné!")
        return True
    else:
        print("Vous avez perdu!")
        return False

jeu_bataille_naval()
