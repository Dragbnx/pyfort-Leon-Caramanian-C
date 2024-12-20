import random

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
    for i in range(1, n): #boucle pour verifier chaque valeurs entre 1 et lui-même
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

def epreuve_math_factorielle():
    """ None -> bool
    implementation d'une epreuve ou le joueur doit trouver la valeur de factiorelle de n
    """
    val = random.randint(1, 10)#choix du nombre entre 1 et 10






"""Fait par moi"""

import random

def  resoudre_equation_lineaire():
    nominateur=random.randint(1,10)
    denominateur=random.randint(1,10)
    #nominateur*solution/denominateur=0
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


print(epreuve_math_equation())


def factorielle(n):
    """ Calcule la factorielle de n (notée n!) """
    for i in range (n) :
        solution = 1
        if n == 0 :
            return
        else :
            solution *= n

def epreuve_math_factorielle():
    """
    créationde de la valeur random factoriel
    """
    val=random.randint(1,10)
    solution = factoriel(val)
    """appel de la fonction générant la réponse. """
    if solution == input(f"Résoudre la factorielle {val}! : "):
        return True
    else :
        return False

print(epreuve_math_factoriel())








