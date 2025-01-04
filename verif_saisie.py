def verification_saisie_entier(saisie):
    """ str -> bool
    renvoie True si la saisie est un entier, False sinon
    """
    if saisie == '': return False
    for elm in saisie:
        if not ord('0') <= ord(elm) <= ord('9'): return False
    return True