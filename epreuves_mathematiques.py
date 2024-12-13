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

def resoudre_equation_lineaire():
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    print(f"Resoudre l'équation : {a}x+{b} =0")
    x = -b/a
    print(x)
    return x


def epreuve_math_equation():
    x = resoudre_equation_lineaire()
    solution_utilisateur = str(input("Quelle est la valeur de x : "))
    cpt = 0
    if solution_utilisateur[0] != '-':
        for i in range (len(solution_utilisateur)):
            cpt += 1
        if valeur == '/':
            break
        i = int(solution_utilisateur[:cpt-1])
        z = int(solution_utilisateur[cpt+1:])
    else:
        return False
    y = solution_utilisateur[cpt+1:] / solution_utilisateur[1:cpt-1]
    if y == x:
        return True
    else:
        return False

