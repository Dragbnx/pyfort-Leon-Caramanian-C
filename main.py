from epreuves_mathematiques import *
from enigme_pere_fouras import *
from epreuves_logiques import *
from epreuve_finale import *
from epreuves_hasard import *
from fonctions_utiles import *





def jeu():
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
    salle_De_tresor()



jeu()