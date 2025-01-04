import random
from verif_saisie import *



def factorielle(n):
    """int -> int
    renvoie la valeur de n! la fonction est code de maniere recursive
    """
    if n == 0: #cas de base
        return 1
    else: #itération pour les n-1
        return n * factorielle(n-1)

def est_premier(n):
    """ int -> bool
    renvoie si n est un nombre premier
    """
    for i in range(2, n): #boucle pour verifier chaque valeurs entre 1 et lui-même
        if n % i == 0:
            return False
    return True

def premier_plus_proche(n):
    """ int -> int
    renvoie le premier nombre premier supérieur ou égal à n
    """
    while not est_premier(n): #iteration tant que n n'est pas premier
        n += 1
    return n



def epreuve_math_premier():
    nb = random.randint(10, 20)
    reponse = premier_plus_proche(nb)
    print(f"Quel est le premier le plus proche de {nb} ?")
    entree = input("Votre réponse est : ")
    while not verification_saisie_entier(entree):
        print("Entree non valide.")
        entree = input("Votre réponse est : ")
    return reponse == int(entree)

def epreuve_math_factorielle():
    """
    créationde de la valeur random factoriel
    """
    val=random.randint(1,10)
    solution = factorielle(val)#appel de la fonction générant la réponse.
    if solution == input(f"Résoudre la factorielle {val}! : "):
        return True
    else :
        return False



def  resoudre_equation_lineaire():
    nominateur=random.randint(1,10)
    denominateur=random.randint(1,10) #nominateur*solution/denominateur=0
    solution = -denominateur/nominateur
    return nominateur,denominateur,solution

def epreuve_math_equation():
    nominateur,denominateur,solution = resoudre_equation_lineaire()
    reponse = (input(f" Soit l'équation {nominateur}x+{denominateur}=0, résoudre l'équation : "))
    reponse = eval(reponse)
    if solution == reponse:
        return True
    else:
        return False


def epreuve_math():
    epreuves = [epreuve_math_equation, epreuve_math_factorielle, epreuve_math_premier]
    epreuve = random.choice(epreuves)
    return epreuve()
