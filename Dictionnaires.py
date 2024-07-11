import json

# charger les données depuis le fichier
with open('classe.json', 'r') as file:
    eleves = json.load(file)

for eleve in eleves:
    print(eleves[eleve]['note'], eleves[eleve]['appreciation'])

# ajouter une eleve
eleves['Léa'] = {
    'note': 10,
    'appreciation': 'Peut mieux faire'
}

#changer une note
eleves["Camille"]['note'] = 20

#verifier qu un eleve existe dans la classe
if 'Théo' in eleves.keys():
    print("Théo est bien dans la classe")
else:
    print("Théo n'est pas dans la classe")

#supprimer un eleve
del eleves['Théo']

if 'Théo' in eleves.keys():
    print("Théo est bien dans la classe")
else:
    print("Théo n'est pas dans la classe")

for eleve in eleves:
    print(eleves[eleve]['note'], eleves[eleve]['appreciation'])

#sauvegarder notre classe dans un fichier
with open('classe.json', 'w+') as file:
    json.dump(eleves, file)
