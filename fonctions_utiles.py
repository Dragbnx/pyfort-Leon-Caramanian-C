from epreuves_mathematiques import *
from enigme_pere_fouras import *
from epreuves_logiques import *
from epreuves_hasard import *
from verif_saisie import *


def introduction():
    """none -> none
    affiche les regles  et dis bienvenue !
    """
    print("Bienvenue sur pyfort ! \nLes régles sont simples, vous devez récuperer 3 clé afin de pouvoir débloquer la salle du trésor...\
     \nUne fois dans la salle du trésor vous devez trouver le mot secret afin de gagner la partie !\
     \nBonne chance a vous !")

def composer_equipes():
    """None -> Table[Dic]
    permet de composer les équipes
    """
    nb = input("Entrer le nombre de joueur entre 1 et 3 : ") #vérification du nombre de joueurs
    joueurs = []
    while not verification_saisie_entier(nb) or not 0 < int(nb) <= 3: #vérification de l'entrée de l'utilisateur
        print("La valeur entrée n'est pas valide")
        nb = input("Entrer le nombre de joueur entre 1 et 3 : ")
    nb = int(nb)
    leaders = False
    for i in range(nb): #remplissage des joueurs
        joueur = {}
        joueur['nom'] = input("Entrer le nom du joueur : ")
        joueur['profession'] = input("Entrer le profession du joueur : ")
        if not leaders: #Vérification du leader
            leader = input('Entrer si le joueur est le leader de l\'équipe (mettre "leader" pour leader, "membre" pour membre): ')
            while leader.lower() != 'leader' and leader.lower() != 'membre':
                print('Valeur invalide. Veuillez entrer "leader" ou "membre.')
                leader = input('Entrer si le joueur est le leader de l\'équipe (mettre "leader" pour leader, "membre" pour membre): ')
            if leader.lower() == 'leader':
                leaders = True
            joueur['leader'] = leader.lower()
        else:
            joueur['leader'] = 'membre'
        joueur['cle'] = 0
        joueurs.append(joueur)
    if not leaders: #premier joueur devient leader si aucun leader
        joueurs[0]['leader'] = 'leader'
    return joueurs

def menu_epreuve():
    """None -> bool
    permet au jouer de choisir son épreuve
    """
    print("1. Épreuve de Mathématiques\
    \n2. Épreuve de Logique\
    \n3. Épreuve du hasard\
    \n4. Énigme du Père Fouras")
    choix = input("Entrer choix : ")
    while not verification_saisie_entier(choix) or not 1 <= int(choix) <= 4:
        print("La valeur n'est pas valide")
        choix = input("Entrer choix : ")
    match choix:
        case '1': return epreuve_math()
        case '2': return jeu_bataille_naval()
        case '3': return epreuves_hasard()
        case '4': return enigme_pere_fouras()


def choisir_joueur(equipe):
    """Table[Dic]-> Dic
    permet de selectionner un joueur d'une equipe
    """
    for i in range(len(equipe)):
        print(f"{i+1}. {equipe[i]['nom']} ({equipe[i]['profession']}) - {equipe[i]['leader']}")
    choix_joueur = input("Entrer le numéro du joueur : ")
    while not verification_saisie_entier(choix_joueur) or not 0 < int(choix_joueur) <= len(equipe) :
        print("La valeur n'est pas valide")
        choix_joueur = input("Entrer le numéro du joueur : ")
    return equipe[int(choix_joueur)-1]



def enregistrer_historique(equipe, resultat):
    """Table[Dic], Bool-> None
    enregistre un historique de la partie d'une equipe
    """
    with open("output/historique.txt", "a", encoding="utf-8") as file:
        for joueur in equipe:
            file.write(f"{joueur['nom']} ({joueur['profession']}) - {joueur['leader']}\n")
            file.write(f"Nombre de cle gagné : {joueur['cle']}\n\n")
        if resultat:
            file.write("Nous avons triompher !\n\n")
        else:
            file.write("Nous avons perdu ! \n\n")
