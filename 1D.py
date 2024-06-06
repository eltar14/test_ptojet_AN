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
# dimensions :
longueur = 11.583
largeur = 2.294
hauteur = 2.567


# Algo de best fit : mettre dans le bin ou il restera le moins de capacite apres l'operation, minimiser la capacite restante
"""class Object:
    def __init__(self,name,  lon, lar, h):
        self.name = name
        self.length = lon
        self.width = lar
        self.height = h

    def print(self):
        print(f'name : {self.name} ; lon : {self.length} ') # ; lar : {self.width} ; h : {self.hauteur}"""


"""class Shelf:
    def __init__(self):
        CONTAINER_LENGTH = 11.583
        self.content = []  # des objects
        self.length = CONTAINER_LENGTH
        self.width = 0 # largeur de la colonne, dépendra de ce qu'il y aura dedans
        self.remaining_length = CONTAINER_LENGTH
        # on verra la largeur disponible en dehors

    def add(self, obj: Object):
        self.content.append(obj)
        self.remaining_length -= obj.length
        self.width = obj.width if obj.width > self.width else self.width

    def print(self):
        print(f'Longueur : {self.length} ; largeur : {self.width} ; remaining : {self.remaining_length}')
        for obj in self.content:
            obj.print()
        print()"""


"""def le2d(objects:list):

    wagons = [] # liste des wagons
    w = Wagon()
    w.add_shelf(Shelf())
    wagons.append(w)

    for o in objects:
        placed = False
        for wagon in wagons:
            for shelf in wagon.content :
                if((o.width <= (wagon.get_remaining_width() + shelf.width)) and (o.length <= shelf.remaining_length)) : # sum(instance.value for instance in instances)
                    shelf.add(o)
                    placed = True
                    break
        if not placed:
            for wagon in wagons:
                if (wagon.get_remaining_width() >= o.width) and (wagon.length >= o.width):
                    s = Shelf()
                    s.add(o)
                    wagon.add_shelf(s)
                    placed = True
        if not placed:
            w = Wagon()
            s = Shelf()
            s.add(o)
            w.add_shelf(s)
            wagons.append(w)
    return wagons"""






class Wagon:
    """
    author : A
    """
    def __init__(self):
        self.content = [] # soit des shelf soit directement des objets
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





def xlsx_to_object_list(path:str):
    """
    author : A
    :param path:
    :return:
    """
    data = pd.read_excel(path)
    data = data.values.tolist()
    objs = []
    for elt in data:
        #print(elt)
        o = Object(*elt[1:])
        objs.append(o)  # liste d'objets
    return objs


def fill_Wagon_1d_online(objects:list):
    """
    author : A
    :param objects:
    :return:
    """
    wagons = []
    wagons.append(Wagon())
    loop_count = 0

    for o in objects:
        loop_count += 1
        remaining_per_w_after = []
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


    b = fill_Wagon_1d_offline(a)
    print(f'{len(b)} wagons')
    for wagon in b:
        wagon.print()

    """start_time = time.time()
    le2d(a)
    end_time = time.time()

    print((end_time-start_time)/1000, "ms")"""




