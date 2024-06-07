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
from Object import Object

from tools import xlsx_to_object_list

# dimensions :
longueur = 11.583
largeur = 2.294
hauteur = 2.567


# Algo de first fit : mettre dans le premier "trou" qui correspond

class Shelf:  # 2D
    """
    author : A
    """
    def __init__(self):
        CONTAINER_LENGTH = 11.583
        self.content = []  # list of Objects
        self.length = CONTAINER_LENGTH
        self.width = 0 # largeur de la colonne, dépendra de ce qu'il y aura dedans # width, will be changed by what s inside
        self.remaining_length = CONTAINER_LENGTH

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
    """
    author : A
    """
    def __init__(self):
        self.content = [] # will contain the shelves
        self.length = 11.583
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
def plot_wagon(wagon):
    """
    plots a single wagon using matplotlib
    author : A
    :param wagon:
    :return:
    """
    fig, ax = plt.subplots(1, 1)

    # set size
    ax.set_xlim(0, 11583)
    ax.set_ylim(0, 2294)
    ax.add_patch(Rectangle((0, 0), 11.583, 2.294, edgecolor="black", facecolor='none')) # add wagon outline

    for sn, shelf in enumerate(wagon.content):
        for en, obj in enumerate(shelf.content): # for each object
            len = sum(o.length for o in shelf.content[:en]) # sum of the length of the previous objects in the shelf
            wid = sum(o.width for o in wagon.content[:sn]) # sum of the width of the previous shelves
            col = (np.random.random(), np.random.random(), np.random.random()) # choose a random color to visualize better
            ax.add_patch(Rectangle((len, wid), obj.length, obj.width, facecolor=col))

    plt.axis('equal') # axis x and y to the same scale
    plt.show()


def plot_wagons(wagons, n_cols=5):
    """
    displays a whole 2 dimensional train using matplotlib

    author : A
    :param wagons:
    :param n_cols:
    :return:
    """
    num_wagons = len(wagons)
    n_rows = (num_wagons + n_cols - 1) // n_cols  # nb of lines needed

    fig, axs = plt.subplots(n_rows, n_cols, figsize=(n_cols * 6, n_rows * 4))

    # if only one wagon ax isnt a list so we convert it into one
    if num_wagons == 1:
        axs = [[axs]]
    elif n_rows == 1:
        axs = [axs]
    elif n_cols == 1:
        axs = [[ax] for ax in axs]

    
    wagon_length = 11.583
    wagon_width = 2.294

    for w_idx, (ax, wagon) in enumerate(zip(axs.flat, wagons)):
        ax.set_xlim(0, wagon_length)
        ax.set_ylim(0, wagon_width)

        # draw wagon edges
        ax.add_patch(Rectangle((0, 0), wagon_length, wagon_width, edgecolor="black", facecolor='none')) # wagon outline

        for sn, shelf in enumerate(wagon.content) :
            for en, obj in enumerate(shelf.content):
                obj_len = sum(o.length for o in shelf.content[:en])  # sum of the length of the previous objects in the shelf
                obj_wid = sum(o.width for o in wagon.content[:sn])  # sum of the width of the previous shelves
                col = (np.random.random(), np.random.random(), np.random.random()) # choose a random color for better visualization
                ax.add_patch(Rectangle((obj_len, obj_wid), obj.length, obj.width, facecolor=col))

        ax.set_aspect('equal')
        ax.set_title(f'Wagon {w_idx + 1}') # Wagon n

        ax.axis('off') # too much things displayed if we leave the axes
    
    for ax in axs.flat[num_wagons:]: # delete/no display non occupied subplots
        ax.set_visible(False)

    plt.tight_layout()
    plt.show()


def fill_Wagon_2d_online_bis(objects:list):
    """
    old version of the function. Not bugget nut not optimized when placing new shelves.

    returns an array of wagons, with all its content
    author : A
    :param objects:
    :return:
    """
    wagons = [] # liste des wagons
    w = Wagon()
    w.add_shelf(Shelf())
    wagons.append(w)

    for index, o in enumerate(objects):
        placed = False
        for wagon in wagons:
            for shelf in wagon.content :
                if((o.width <= (wagon.get_remaining_width() + shelf.width)) and (o.length <= shelf.remaining_length)) : # sum(instance.value for instance in instances)
                    shelf.add(o) # if it fits in an existing shelf
                    #print(index, "a")
                    placed = True
                if placed:
                    break
            if placed:
                break


        if not placed:
            for wagon in wagons:
                if (wagon.get_remaining_width() >= o.width) and (wagon.length >= o.length): # if it fits in an already existing wagon
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


def fill_Wagon_2d_online(objects:list):
    """
    returns an array of wagon with all their contents
    author : A
    :param objects:
    :return:
    """
    wagons = [] # liste des wagons
    w = Wagon()
    w.add_shelf(Shelf())
    wagons.append(w)

    for index, o in enumerate(objects):
        placed = False
        for wagon in wagons:
            for shelf in wagon.content :
                if((o.width <= (wagon.get_remaining_width() + shelf.width)) and (o.length <= shelf.remaining_length)) :
                    shelf.add(o) # if it fits in an existing shelf
                    #print(index, "a")
                    placed = True
                if placed:
                    break
            if (wagon.get_remaining_width() >= o.width) and (wagon.length >= o.length):  # if it fits in an already existing wagon
                s = Shelf()
                s.add(o)
                wagon.add_shelf(s)
                # print(index, "b")
                placed = True
            if placed:
                break

        if not placed:  # else we need a new wagon
            w = Wagon()
            s = Shelf()
            s.add(o)
            w.add_shelf(s)
            wagons.append(w)
            #print(index, "c")
    return wagons


def fill_Wagon_2d_offline(objects:list):
    """
    fill a 2D train + we can control the input
    author : A
    :param objects:
    :return:
    """
    #objects = sorted(objects, key=lambda k: k.width, reverse=True)  # par ordre décroissant
    objects = sorted(objects, key=lambda k: [k.width, k.length], reverse=True)  # better

    # key = lambda x: (x[column_number_1], x[column_number_2])
    return fill_Wagon_2d_online(objects)


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

    b = fill_Wagon_2d_offline(a)
    end = time.time()
    delta = end-start
    print(f'TIME ELAPSED : { delta}')
    occup_surf = 0
    for wagon in b:
        for s in wagon.content:
            occup_surf += sum(o.length*o.width for o in s.content)

    print(f'Occup s { occup_surf}')
    surf_tot = len(b)*longueur*largeur
    print(f'surf tot {surf_tot}')

    print(f'Ratio occupation surface : { occup_surf/surf_tot}')


    print(f'{len(b)} wagons')
    """for wagon in b:
        wagon.print()"""

    print(type(b))
    #plot_train(b, len(b))
    #plot_wagon2(b[0])
    aaaaa = 0

    plot_wagons(b)
    """for w in b:
        plot_wagon(w)
        aaaaa+=1"""

    """start_time = time.time()
    le2d(a)
    end_time = time.time()

    print((end_time-start_time)/1000, "ms")"""




