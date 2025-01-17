import random
import time


def jeu_des():
    """None -> Bool
     simule le jeu de dés
    """
    print("Voici les règles du jeu : \n\
Vous allez lancer deux dés et si au moins l'un d'eux tombent sur 6 vous remporter la victoire. \n\
Si vous échouez le tour revient au maître.\n\
Si il gagne le match est alors terminé et ainsi de suite. \n\
Le match se termine aussi par une défaite si au bout de 3 tentive vous n'arrivez pas à gagner.")  # Commençons le jeu en affichant les régles
    tentative = 3  # Initialisation du nombre de tentative
    while tentative >= 1:
        # Annoncer le nombre de tentative restante ainsi que les instructions pour joue
        print("il vous reste {} tentative. ".format(tentative))
        # Indiquation de la façcon dont le joueur doit jouer
        lancé = (input('Lancer le dé avec la touche " entrer " '))
        # Création aléatoire des résultats des dés
        stockage_joueur = (random.randint(1, 6), random.randint(1, 6))
        # Affichage des résultats
        print("Votre premier dé est un {} et le deuxiéme est un {}.\n".format(stockage_joueur[0], stockage_joueur[1]))
        # Vérification de la réussite
        for i in range(2):
            if stockage_joueur[i] == 6:
                # Annonce de la victoire
                print("Vous avez eu un 6, vous avez gagnez !")
                return True
        time.sleep(1)
        # Même procédé mais automatisé pour le tour du maître
        stockage_maitre = (random.randint(1, 6), random.randint(1, 6))
        print("Le premier dé du maître est un {} et le deuxiéme est un {}.\n".format(stockage_maitre[0], stockage_maitre[1]))
        for i in range(2):
            if stockage_maitre[i] == 6:
                print("Il a obtenu un 6, vous avez perdu ! ")
                return False
        # Abaissage du nombre de tentative
        time.sleep(1)
        tentative -= 1
    # Afficher la défaite en cas de manque de tentative
    print("Vous n'avez plus de tentative. L'épreuve est donc terminé.")
    return False


def placement_bonneteau():
    """None -> str
    permet de placer la cle sous un bonneteau
     """
    # tirage du banneteau avec la clé
    gobelet = random.randint(1, 3)
    if gobelet == 1:
        solution = "A"
    elif gobelet == 2:
        solution = "B"
    else:
        solution = "C"
    return solution


def bonneteau():
    """None -> bool
    simule le jeu du bonneteau
    """
    print("Vous avez 2 tentatives pour réussir le challenge. \n\
    Vous devez trouver la clé placé sous le bonneteau  ")
    # initialisation du nombre de tentative
    tentative = 2
    # vérification qu'il reste bien des tentatives avant de lui faire refaire l'épreuve
    while tentative >= 1:
        # mise à jour du placement de la clé
        solution = placement_bonneteau()
        # mise à jour du nombre de tentative
        tentative -= 1
        # demande de la réponse de l'utilisateur
        reponse = str(input("Nouvelle tentative. Soit trois bonneteau : A, B et C. Sous quel bonneteau est la clé ? "))
        # comparaison de la reponse de l'utilisateur avec la solution
        if solution == reponse.upper():
            # S'arreter si la tentative et bonne
            print("Bravo ! Vous avez trouvé la clé !")
            return True
    # Si pas de bonne tentive renvoyer que c'est un échec
    print(f"Vous avez perdu, la clé etait sous le bonneteau {solution} ! ")
    return False


def epreuves_hasard():
    """None -> bool
    choisi une epreuve depuis epreuves pour le joueur
    """
    epreuves = [jeu_des, bonneteau]
    epreuve = random.choice(epreuves)
    return epreuve()
