from epreuve_finale import *
from fonctions_utiles import *


def jeu():
    """None -> None
    permet de faire tourner le jeu, avec la création de d'equipe et la gestion d'epreuve
    """
    introduction()
    equipes = composer_equipes()
    nb_cle = 0
    while not nb_cle == 3:
        joueur = choisir_joueur(equipes)
        result = menu_epreuve()
        if result:
            joueur['cle'] += 1
            nb_cle += 1
            print(f"Bravo, vous avez {nb_cle} clé")
        else:
            print("Raté !")
    result = salle_De_tresor()
    enregistrer_historique(equipes, result)


jeu()
