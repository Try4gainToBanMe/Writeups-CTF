import sys # <- L'import du package  pour run python 
import math

light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]

while True:
    remaining_turns = int(input())

    directions = ""

    if initial_ty > light_y:
        directions += "N"
        initial_ty -= 1
    elif initial_ty < light_y:
        directions += "S"
        initial_ty += 1

    if initial_tx < light_x:
        directions += "E"
        initial_tx += 1
    elif initial_tx > light_x:
        directions += "W"
        initial_tx -= 1

    print(directions)
    
    #Mon raisonnement ELI5 
    
    #initial = Thor // light = lumière
    
    # Mon raisonnement (ligne 18) : Si initial_tx est inférieur à light_x Alors Thor est à gauche de l'éclair (light) Donc +1 en Est

# Même principe si initial_tx est supérieur à light_x alors Thor est à droite de l'éclair Donc - 1 en OUEST

# J'ai crée la variable directions au début de chaque itération de la boucle, la variable "directions" initialisée à une chaîne vide (""). Ensuite, sa valeur varie en fonction de la position actuelle de Thor par rapport à la lumière 