import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np


# dimensions :
longueur = 11.583
largeur = 2.294
hauteur = 2.567


class Object:
    def __init__(self,name,  lon, lar, h):
        self.name = name
        self.length = lon
        self.width = lar
        self.height = h

    def print(self):
        print(f'name : {self.name} ; lon : {self.length} ; lar : {self.width} ; h : {self.height}') # ; lar : {self.width} ; h : {self.hauteur}
        
        
class Saucisse:
    def __init__(self):
        CONTAINER_LENGTH = 11.583
        
        self.content = []
        self.length = CONTAINER_LENGTH
        self.width = 0
        self.height = 0
        self.remaining_length = CONTAINER_LENGTH
        
        
    def add(self, obj:Object):
        self.content.append(obj) # list of objects
        self.remaining_length-= obj.length
        self.width = obj.width if obj.width > self.width else self.width
        self.height = obj.height if obj.height > self.height else self.height

    def print(self):
        print(f'Longueur : {self.length} ; largeur : {self.width} ; hauteur : {self.height} ; remaining length inside : {self.remaining_length}')
        for obj in self.content:
            obj.print()
        print()


class Shelf():
    def __init__(self):
        CONTAINER_LENGTH = 11.583
        CONTAINER_WIDTH = 2.294
        CONTAINER_HEIGHT = 2.567 # seule variable pour une shelf

        self.saucisses = [] # list of Saucisses
        self.length = CONTAINER_LENGTH
        self.width = CONTAINER_WIDTH
        self.height = 0
        # self.remaining_height = CONTAINER_HEIGHT # a calculer dynamiquement, en fonction des shelf d'en dessous / dessus

    def add(self, obj:Saucisse): # add a Saucisse object
        self.saucisses.append(obj) # list of objects
        # remaining height ? à faire en dehors car depend des shelf en dessous et dessus
        self.height = obj.height if obj.height > self.height else self.height # height of the Shelf

    def get_remaining_width(self):
        return self.width - (sum(sh.width for sh in self.saucisses))

    def print(self): # print les saucisses
        print(f'SHELF  ===:::===   Longueur : {self.length} ; largeur : {self.width}')
        for sauc in self.saucisses:
            sauc.print()
        print()

    def get_remaining_width(self):
        return self.width - (sum(sauc.width for sauc in self.saucisses))

class Wagon:
    def __init__(self):
        self.shelves = [] # liste des shelves dans le wagon
        self.length = 11.583 # capacity
        self.width = 2.294
        self.height = 2.567

        self.remaining_height = self.height

    def add(self, obj:Shelf): # to add a shelf
        self.shelves.append(obj)
        self.remaining_height -= obj.height # hauteur restante pour une shelf

    def get_remaining_height(self):
        return self.height - (sum(sh.height for sh in self.shelves))

    def print(self):
        print(f'WAGON :   ---===:::===---   Longueur : {self.length} ; remaining_height : {self.remaining_height}')
        for shelf in self.shelves:
            shelf.print()
        print()
        print()
        print()




def la3d(objects:list[Object]):
    wagons = []  # liste des wagons
    
    sauc = Saucisse()
    shel = Shelf()
    shel.add(sauc)
    w = Wagon()
    w.add(shel)
    wagons.append(w)
    placed = False
    for o in objects:
        print("OOOOOb")
        for wagon in wagons:
            for shelf in wagon.shelves:
                for saucisse in shelf.saucisses:
                    if  o.length <= saucisse.remaining_length and o.width <= (shelf.get_remaining_width() + saucisse.width) and o.height <= (wagon.get_remaining_height() + shelf.height):
                        saucisse.add(o)
                        placed = True
                        print("a")

                    if placed:
                        break
                if placed:
                    break
            if placed:
                break
        if not placed: # add saucisse ?  need new saucisse
            for wagon in wagons:
                for shelf in wagon.shelves:
                    if o.width <= shelf.get_remaining_width() + shelf.width and o.height <= (wagon.get_remaining_height() + shelf.height):
                        s = Saucisse()
                        s.add(o)
                        shelf.add(s)
                        placed = True
                        print("b")
                    if placed:
                        break
                if placed:
                    break

        if not placed: # need new shelf
            for wagon in wagons:
                if o.height <= wagon.get_remaining_height():
                    sauc = Saucisse()
                    sauc.add(o)

                    s = Shelf()
                    s.add(sauc)

                    wagon.add(s)

                    placed = True
                    print("c")
                if placed:
                    break

        if not placed: # need new wagon
            sauc = Saucisse()
            sauc.add(o)

            sh = Shelf()
            sh.add(sauc)

            w = Wagon()
            w.add(sh)

            wagons.append(w)
            placed = True
            print("d")

    return wagons


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
    a = xlsx_to_object_list("Données marchandises.xlsx")
    print(len(a[:3]))
    b = la3d(a[:3])


    for w in b:
        w.print()