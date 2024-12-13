from fonctions_utiles import verification_saisie_entier




def suiv(joueur):
    """int -> int
    Renvoie le joueur suivant
    """
    if joueur == 0: return 1
    return 0

def grille_vide():
    return [[" " for _ in range(3)] for _ in range(3)]

def affiche_grille(grille, message):
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
    print("Bateau 1")
    x, y = demande_position()
    while not grille[x][y] == " ":
        print("position déja occupé")
        x, y = demande_position()
    grille[x][y] = 'B'
    print("Bateau 2")
    x, y = demande_position()
    while not grille[x][y] == " ":
        print("position déja occupé")
        x, y = demande_position()
    grille[x][y] = 'B'
    return grille

def tour():
    pass