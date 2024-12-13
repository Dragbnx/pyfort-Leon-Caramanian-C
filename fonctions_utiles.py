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

def verification_saisie_entier(saisie):
    """ str -> bool
    renvoie True si la saisie est un entier, False sinon
    """
    for elm in saisie:
        if not ord('0') <= ord(elm) <= ord('9'):
            return False
    return True
