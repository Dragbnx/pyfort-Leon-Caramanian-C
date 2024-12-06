from fonctions_utiles import factorielle, est_premier
import random

def epreuve_math_factorielle():
    """ None -> bool
    implementation d'une epreuve ou le joueur doit trouver la valeur de factiorelle de n
    """
    val = random.randint(1, 10)#choix du nombre entre 1 et 10