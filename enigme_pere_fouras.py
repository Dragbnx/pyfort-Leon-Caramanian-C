import json, random

def charger_enigmes(fichier):
    enigme = []
    with open(fichier, "r", encoding="utf-8") as file:
        data = json.load(file)
    for elm in data:
        enigme.append({elm['question']:elm['reponse']})
    return enigme


def enigme_pere_fouras():
    enigmes = charger_enigmes("data/enigmesPF.json")
    enigme = random.choice(enigmes)
    essaie = 3
    q = list(enigme.keys())[0]
    r = enigme[q]
    print(q)
    while essaie >= 0:
        reponse = input("Entrer votre reponse : ").lower()
        if r.lower() == reponse:
            print("Votre réponse est correcte !")
            return True
        else:
            essaie -= 1
            if essaie == 0:
                print(f"Vous avez échouer, la réponse etait : {r}")
                return False
            else:
                print(f"Votre réponse est fausse, il vous reste {essaie} réponse")
