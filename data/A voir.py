import random

def resoudre_equation_lineaire():
    #génération des termes de l'équation
    terme1=random.randint(1,10)
    terme2=random.randint(1,10)
    #terme1*solution+terme2=0
    solution = -terme2/terme1
    return terme1,terme2,solution

def epreuve_math_equation():
    #déterminer la solution
    terme1,terme2,solution = resoudre_equation_lineaire()
    #demande à l'utilisateur quel est sa réponse
    reponse = (input(f" Soit l'équation {terme1}x+{terme2}=0, résoudre l'équation : "))
    reponse = eval(reponse)
    #comparer la réponse de l'utilisateur avec la bonne réponse
    if solution == reponse:
        return True
    else:
        return False

#print(epreuve_math_equation())


def factorielle(n):
    """ Calcule la factorielle de n (notée n!) """
    if n == 0 :
        return 1
    solution = 1
    for i in range (1,n+1) :
        solution *= i
    return solution

def epreuve_math_factorielle():
    #création de la valeur random factorielle
    val=random.randint(1,10)
    #appel de la fonction générant la réponse et comparaison avec la réponse de l'utilisateur
    if factorielle(val) == eval(input(f"Résoudre la factorielle {val}! : ")):
        return True
    else :
        return False

#print(epreuve_math_factorielle())



def placement_banneteau():
    #tirage du banneteau avec la clé
    gobelet = random.randint(1,3)
    if gobelet == 1 :
        solution = "a"
    elif gobelet == 2 :
        solution = "b"
    else :
        solution = "c"
    return solution

def banneteau():
    print("Vous avez 2 tentatives pour réussir le challenge.")
    #initialisation du nombre de tentative
    tentative = 0
    #vérification qu'il reste bien des tentatives avant de lui faire refaire l'épreuve
    while tentative <= 1 :
        #mise à jour du placement de la clé
        solution = placement_banneteau()
        #mise à jour du nombre de tentative
        tentative += 1
        #demande de la réponse de l'utilisateur
        reponse = input("Nouvelle tentative. Soit trois baneteau : a, b et c. Sous quel banneteau est la clé ? ")
        #comparaison de la reponse de l'utilisateur avec la solution
        if solution == reponse:
            #S'arreter si la tentative et bonne
            return True
    #Si pas de bonne tentive renvoyer que c'est un échec
    return False

#print(banneteau())