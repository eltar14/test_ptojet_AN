#   /$$$$$$              /$$ /$$                                             /$$
#  /$$__  $$            | $$|__/                                            |__/
# |__/  \ $$        /$$$$$$$ /$$ /$$$$$$/$$$$   /$$$$$$  /$$$$$$$   /$$$$$$$ /$$  /$$$$$$  /$$$$$$$   /$$$$$$$
#   /$$$$$$/       /$$__  $$| $$| $$_  $$_  $$ /$$__  $$| $$__  $$ /$$_____/| $$ /$$__  $$| $$__  $$ /$$_____/
#  /$$____/       | $$  | $$| $$| $$ \ $$ \ $$| $$$$$$$$| $$  \ $$|  $$$$$$ | $$| $$  \ $$| $$  \ $$|  $$$$$$
# | $$            | $$  | $$| $$| $$ | $$ | $$| $$_____/| $$  | $$ \____  $$| $$| $$  | $$| $$  | $$ \____  $$
# | $$$$$$$$      |  $$$$$$$| $$| $$ | $$ | $$|  $$$$$$$| $$  | $$ /$$$$$$$/| $$|  $$$$$$/| $$  | $$ /$$$$$$$/
# |________/       \_______/|__/|__/ |__/ |__/ \_______/|__/  |__/|_______/ |__/ \______/ |__/  |__/|_______/

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np

# dimensions :
longueur = 11.583
largeur = 2.294
hauteur = 2.567


# Algo de first fit : mettre dans le premier trou qui correspond
class Object:
    def __init__(self,name,  lon, lar, h):
        self.name = name
        self.length = lon
        self.width = lar
        self.height = h

    def print(self):
        print(f'name : {self.name} ; lon : {self.length} ; lar : {self.width}') # ; lar : {self.width} ; h : {self.hauteur}


class Shelf:  # 2D
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
        print()

class Wagon:
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
        for shelf in self.content:
            shelf.print()
        print()
        print()
        print()
"""def fill_Wagon_2d_online(objects:list):
    wagons = [] # liste des wagons
    w = Wagon()
    w.add_shelf(Shelf())
    wagons.append(w)
    index = 0
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
                    break
        if not placed:
            w = Wagon()
            s = Shelf()
            s.add(o)
            w.add_shelf(s)
            wagons.append(w)
        index +=1
    return wagons"""








"""def plot_wagons(wagons):
   for i, wagon in enumerate(wagons):
       # Créer une nouvelle figure pour chaque wagon
       fig, ax = plt.subplots()

       # Définir les limites de la figure pour correspondre à la taille du wagon
       ax.set_xlim(0, 11583)
       ax.set_ylim(0, 2294)

       # Ajouter un rectangle pour chaque objet dans le wagon
       x = 0  # position x de l'objet actuel
       for obj in wagon:
           # Ajouter un rectangle avec la position et la taille de l'objet
           rect = patches.Rectangle((x, 0), obj[1], obj[2], linewidth=1, edgecolor='r', facecolor='none')
           ax.add_patch(rect)

           # Ajouter le nom de l'objet au centre du rectangle
           ax.text(x + obj[1] / 2, obj[2] / 2, obj[0], ha='center', va='center')

           # Mettre à jour la position x pour l'objet suivant
           x += obj[1]

       # Afficher la figure
       plt.axis('equal')
       plt.show()"""

def plot_wagons(wagons:list):
    plots = []
    for i, wagon in enumerate(wagons):
        plots[i] = fig, ax = plt.subplots()

        # Définir les limites de la figure pour correspondre à la taille du wagon
        ax.set_xlim(0, 11583)
        ax.set_ylim(0, 2294)

        for sn, shelf in enumerate(wagon.content):
            for en, obj in enumerate(shelf.content):
                len = sum(o.length for o in shelf.content[:en])  # somme des longueurs jusqu a l index en
                wid = sum(o.width for o in shelf.content[:en])
                ax.add_patch(Rectangle((len, wid), obj.length, obj.width, edgecolor='orange', linewidth=2))
        break

    plt.plot()

def plot_wagon(wagon, iter = 0):
        fig, ax = plt.subplots(1, 1)

        # Définir les limites de la figure pour correspondre à la taille du wagon
        ax.set_xlim(0, 11583)
        ax.set_ylim(0, 2294)
        ax.add_patch(Rectangle((0, 0), 11.583, 2.294, edgecolor="black", facecolor='none'))

        for sn, shelf in enumerate(wagon.content):
            for en, obj in enumerate(shelf.content):
                len = sum(o.length for o in shelf.content[:en]) # somme des longueurs jusqu a l index en
                wid = sum(o.width for o in wagon.content[:sn]) # hauteur des shelves en dessous
                col = (np.random.random(), np.random.random(), np.random.random())
                ax.add_patch(Rectangle((len, wid), obj.length, obj.width, facecolor=col))

        plt.axis('equal')
        plt.show()

def plot_train(wagons, len):
    fig, ax = plt.subplots(1, len)
    for index, wagon in enumerate(wagons):
        print(index)
        # Définir les limites de la figure pour correspondre à la taille du wagon
        #ax[index].set_xlim(0, 11583)
        #ax[index].set_ylim(0, 2294)
        ax[index].add_patch(Rectangle((0, 0), 11.583, 2.294, edgecolor="black", facecolor='none'))

        for sn, shelf in enumerate(wagon.content):
            for en, obj in enumerate(shelf.content):
                len = sum(o.length for o in shelf.content[:en])  # somme des longueurs jusqu a l index en
                wid = sum(o.width for o in wagon.content[:sn])  # hauteur des shelves en dessous
                col = (np.random.random(), np.random.random(), np.random.random())
                ax[index].add_patch(Rectangle((len, wid), obj.length, obj.width, facecolor=col))

        plt.axis('equal')
    plt.show()

def fill_Wagon_2d_online(objects:list):
    wagons = [] # liste des wagons
    w = Wagon()
    w.add_shelf(Shelf())
    wagons.append(w)

    for index, o in enumerate(objects):
        placed = False
        for wagon in wagons:
            for shelf in wagon.content :
                if((o.width <= (wagon.get_remaining_width() + shelf.width)) and (o.length <= shelf.remaining_length)) : # sum(instance.value for instance in instances)
                    shelf.add(o)
                    #print(index, "a")
                    placed = True
                if placed:
                    break
            if placed:
                break


        if not placed:
            for wagon in wagons:
                if (wagon.get_remaining_width() >= o.width) and (wagon.length >= o.width):
                    s = Shelf()
                    s.add(o)
                    wagon.add_shelf(s)
                    #print(index, "b")
                    placed = True
                    break
        if not placed:
            w = Wagon()
            s = Shelf()
            s.add(o)
            w.add_shelf(s)
            wagons.append(w)
            #print(index, "c")
    return wagons

def fill_Wagon_2d_offline(objects:list):
    objects = sorted(objects, key=lambda k: k.width, reverse=True)  # par ordre décroissant
    return fill_Wagon_2d_online(objects)

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


    b = fill_Wagon_2d_offline(a)
    print(f'{len(b)} wagons')
    """for wagon in b:
        wagon.print()"""

    print(type(b))
    #plot_train(b, len(b))
    #plot_wagon2(b[0])
    aaaaa = 0
    for w in b:
        plot_wagon(w)
        aaaaa+=1

    """start_time = time.time()
    le2d(a)
    end_time = time.time()

    print((end_time-start_time)/1000, "ms")"""




