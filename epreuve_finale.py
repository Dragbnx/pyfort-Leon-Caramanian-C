import json
import random


def charger_indices_salle(fichier):
    """str -> dic
    charge les indices du fichier en dictionnaire
    """
    with open(fichier, 'r', encoding='utf-8') as f:
        return json.load(f)


def salle_De_tresor():
    """None-> Bool
    simule l'etape du trésor
    """
    data = charger_indices_salle('data/indicesSalle.json')
    annee = random.choice(list(data['Fort Boyard'].keys()))
    emission = random.choice(list(data['Fort Boyard'][annee].keys()))
    indices = data['Fort Boyard'][annee][emission]['Indices']
    mot_code = data['Fort Boyard'][annee][emission]['MOT-CODE']
    print("Bienvenue dans la salle du trésor !")
    print(f"Année : {annee}, Émission : {emission}")
    print("Voici les trois premiers indices pour vous aider :")
    for i in range(3):
        print(f"- {indices[i]}")
    essais = 3
    indice_actuel = 3
    reponse_correcte = False
    while essais > 0 and reponse_correcte == False:
        reponse = input("Quel est votre mot-code ? ").upper()
        if reponse == mot_code:
            reponse_correcte = True
        else:
            essais -= 1
            print(f"Incorrect. Il vous reste {essais} essai(s).")
            if essais > 0 and indice_actuel < len(indices):
                print(f"Indice supplémentaire : {indices[indice_actuel]}")
                indice_actuel += 1
    if reponse_correcte:
        print("Félicitations ! Vous avez trouvé le mot-code et accédez au trésor !")
        return True
    else:
        print(f"Vous avez échoué. Le mot-code était : {mot_code}.")
        return False