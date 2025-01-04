def verification_saisie_entier(saisie):
    """ str -> bool
    renvoie True si la saisie est un entier, False sinon
    """
    if saisie == '': return False
    for elm in saisie:
        if not ord('0') <= ord(elm) <= ord('9'): return False
    return True



def introduction():
    """none -> none
    affiche les regles  et dis bienvenu !
    """
    print("Bienvenue sur pyfort ! \nLes régles sont simples, vous devez récuperer 3 clé afin de pouvoir débloquer la salle du trésor...\
     \nUne fois dans la salle du trésor vous devez trouver le mot secret afin de gagner la partie !\
     \nBonne chance a vous !")

def composer_equipes():
    """None -> Table[Dic]
    permet de composer les équipes
    """
    nb = input("Entrer le nombre de joueur entre 1 et 3 : ") #vérification de
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
    print("1. Épreuve de Mathématiques\
    \n2. Épreuve de Logique\
    \n3. Épreuve du hasard\
    \n4. Énigme du Père Fouras")
    choix = input("Entrer choix : ")
    while not verification_saisie_entier(choix) or not 1 <= int(choix) <= 4:
        print("La valeur n'est pas valide")
        choix = input("Entrer choix : ")
    return choix


def choisir_joueur(equipe):
    for i in range(len(equipe)):
        print(f"{i+1}. {equipe[i]['nom']} ({equipe[i]['profession']}) - {equipe[i]['leader']}")
    choix_joueur = input("Entrer le numéro du joueur : ")
    while not verification_saisie_entier(choix_joueur) or not 0 < int(choix_joueur) <= len(equipe) :
        print("La valeur n'est pas valide")
        choix_joueur = input("Entrer le numéro du joueur : ")
    return equipe[int(choix_joueur)]



def enregistrer_historique(equipe):
    pass