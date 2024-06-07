#    /$$               /$$ /$$                                             /$$
#  /$$$$              | $$|__/                                            |__/
# |_  $$          /$$$$$$$ /$$ /$$$$$$/$$$$   /$$$$$$  /$$$$$$$   /$$$$$$$ /$$  /$$$$$$  /$$$$$$$
#   | $$         /$$__  $$| $$| $$_  $$_  $$ /$$__  $$| $$__  $$ /$$_____/| $$ /$$__  $$| $$__  $$
#   | $$        | $$  | $$| $$| $$ \ $$ \ $$| $$$$$$$$| $$  \ $$|  $$$$$$ | $$| $$  \ $$| $$  \ $$
#   | $$        | $$  | $$| $$| $$ | $$ | $$| $$_____/| $$  | $$ \____  $$| $$| $$  | $$| $$  | $$
#  /$$$$$$      |  $$$$$$$| $$| $$ | $$ | $$|  $$$$$$$| $$  | $$ /$$$$$$$/| $$|  $$$$$$/| $$  | $$
# |______/       \_______/|__/|__/ |__/ |__/ \_______/|__/  |__/|_______/ |__/ \______/ |__/  |__/

import pandas as pd
from Object import Object
from tools import xlsx_to_object_list
# dimensions :
longueur = 11.583
largeur = 2.294
hauteur = 2.567


# Algo de best fit : mettre dans le bin ou il restera le moins de capacite apres l'operation, minimiser la capacite restante


class Wagon:
    """
    author : A
    """
    def __init__(self):
        self.content = []
        self.length = 11.583 # capacity
        self.width = 2.294
        self.height = 2.567
        self.remaining_length = self.length

    def add(self, obj) :
        self.content.append(obj)
        self.remaining_length -= obj.length

    def add_shelf(self, shelf):
        self.content.append(shelf)

    def get_remaining_width(self):
        return self.width-(sum(sh.width for sh in self.content))
    def print(self):
        print(f'Longueur : {self.length} ; remaining_length : {self.remaining_length}')
        for obj in self.content:
            obj.print()
        print()








def fill_Wagon_1d_online(objects:list):
    """
    fills a 1 dimentional train with objects
    returns an array of Wagon
    author : A
    :param objects:
    :return:
    """
    wagons = []
    wagons.append(Wagon())

    for o in objects:
        remaining_per_w_after = [] # remainng width per wagon, index is wagon index
        for wagon in wagons: # calcul des capacités par w apres avoir ajoute o
            remaining_per_w_after.append(wagon.remaining_length - o.length)

        if any(i > 0 for i in remaining_per_w_after): # s il y a assez de place dans l'un ou plus d'entre eux
            best_wagon = remaining_per_w_after.index(min(i for i in remaining_per_w_after if i > 0)) # donne le wagon dans lequel placer le truc par son index
            wagons[best_wagon].add(o)

        else: # si on a pas la place dans les wagons existants
            wt = Wagon()
            wt.add(o)
            wagons.append(wt)

    return wagons

def fill_Wagon_1d_offline(objects:list):
    """
    author : A
    :param objects:
    :return:
    """
    objects = sorted(objects, key=lambda k: k.length, reverse=True) # par ordre décroissant
    return fill_Wagon_1d_online(objects)

if __name__ == '__main__':
    import time
    a = xlsx_to_object_list("Données marchandises.xlsx")
    """
     for elt in a:
        elt.print()
    """

    """
    a = [-2, -44, -5, -1, -223, -2, -1, -7]
    print(min(i for i in a if i > 0))
    """

    start = time.time()
    b = fill_Wagon_1d_offline(a)
    end = time.time()
    delta = end-start
    print(f'TIME ELAPSED : { delta}')
    print(f'{len(b)} wagons')
    for wagon in b:
        wagon.print()
    rest = sum(w.remaining_length for w in b)
    print (rest)
    print(f'len train : {len(b)*longueur}')

    ratio_remplissage = (len(b)*longueur-rest)/(len(b)*longueur)
    print(f'ratio remplissage : {ratio_remplissage}')
    """start_time = time.time()
    le2d(a)
    end_time = time.time()

    print((end_time-start_time)/1000, "ms")"""




