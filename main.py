import pandas as pd
import time
import math
from Objet import Objet
from Bag import Bag
from BinaryTree import BinaryTree
import numpy as np


# PARTIE 1

def algo_concon(objects_list:list, backpack_size:float): # 19 op
    """
    author : A
    :param objects_list:
    :param backpack_size:
    :return:
    """
    sac = []
    #print(objects_list)
    p = 0
    i=0
    while(p+objects_list[i][1]<backpack_size):# 2 op
        sac.append(objects_list[i][0]) # 1op
        p+= objects_list[i][1] # 1 op
        i+=1 # 1 op

    #print(f'Elements dans le sac : {sac}\nPoids : {p}')



def brute_force_binary(objects_list:list, backpack_size:float):
    """
    tests all the possible combinations and returns the bag with the highest score

    author : A
    :param objects_list: list oh Objects, the available objects to put in the bag
    :param backpack_size: maximum bag mass/weight
    :return:
    """
    bags = []
    for i in range(2**len(objects_list)-1):
        bag = Bag()
        binaire_sans_prefixe = bin(i)[2:].zfill(len(objects_list)) # converts i to binary and adds 0s to fll up
        for j in range(len(objects_list)):
            if(int(binaire_sans_prefixe[j]) == 1): # the 0s and 1s are used as booleans
                bag.add(objects_list[j])
        if(bag.weight <= (backpack_size+0.005)): # +epsilon for python floating point error
            bags.append(bag)
    return max(bags, key=lambda k: k.score)


def glouton(objects_list:list, backpack_size:float):
    """
    author : A
    :param objects_list:
    :param backpack_size:
    :return:
    """
    EPSILON = 0.00001
    sorted_by_ratio = sorted(objects_list, key=lambda k: k.ratio(), reverse=True)
    bag = Bag()
    i = 0
    while((bag.weight + sorted_by_ratio[i].masse) < backpack_size + EPSILON):
        bag.add(sorted_by_ratio[i])
        i+=1
    return bag

def branch(objs:list, backpack_size:float):
    """
    author : A
    :param objects_list:
    :param backpack_size:
    :return:
    """
    # TODO objs != objects_list ???
    root = BinaryTree(0)
    root.create_tree(objs, backpack_size)
    vals = root.find_max()[1].get_parents_by_level()[1:]
    out = [obj for flag, obj in zip(vals, objs) if flag == 1]

    stats_sac = [0, 0]
    for elt in out:
        stats_sac[0] += elt.masse
        stats_sac[1] += elt.utilite

    bag = Bag()
    for elt in out:
        bag.add(elt)
    return bag



def dynamique(objets, maxmass):
    """
    author : nathan
    :param objets:
    :param maxmass:
    :return:
    """
    # multiplication par 100 pour ne pas avoir de float
    for obj in objets:
        obj.masse = int(obj.masse * 100)
        obj.utilite = int(obj.utilite * 100)

    maxmass = int(maxmass * 100)

    # création tableau avec des 0
    tab = [[0 for _ in range(maxmass + 1)] for _ in range(len(objets) + 1)]


    for i in range(1, len(objets) + 1):
        for w in range(maxmass + 1):

            if objets[i - 1].masse <= w:
                # on trouve le cas qui à le plus de valeur entre l'itération dernière et celle en cours
                tab[i][w] = max(tab[i - 1][w], tab[i - 1][w - objets[i - 1].masse] + objets[i - 1].utilite)
            else:
                tab[i][w] = tab[i - 1][w]

    # Reconstruire la solution pour trouver quels objets sont inclus
    bag = Bag()
    w = maxmass
    for i in range(len(objets), 0, -1): # parcours des objets en sens inverse
        if tab[i][w] != tab[i - 1][w]: # si différent c'est qu'a cet indice l'objet ajouté est optimale

            bag.add(objets[i - 1])
            w -= objets[i - 1].masse # on réduit la taille restante dans le sac

    # on divise par 100 pour retrouver nos valeurs de bases
    for obj in bag.content:
        obj.masse /= 100
        obj.utilite /= 100
    bag.weight /= 100
    bag.score /= 100

    return bag








# def brute_force_demo():
#     data = pd.read_csv("sac2.csv", sep=';', decimal=',')
#     data = data.values.tolist()
#     objs = []
#     for elt in data:
#         #print(*elt)
#         o = Objet(*elt)
#         objs.append(o)
#     start_time = time.time()
#     b = brute_force_avec_Obj(objs, 0.6)
#     end_time = time.time()
#     print(len(b))
#     best = max(b, key=lambda k: k.score)
#     best.print()
#     print(f'Temps d\'exécution en secondes pour  * la fonc: {(end_time - start_time) / 1}; en ms : {(end_time - start_time) * 1000 / 1}')

# https://www.youtube.com/watch?v=CwM-Mv0Bm4Y


if __name__ == '__main__':

    # mise en forme des données
    data = pd.read_csv("sac2.csv", sep=';', decimal=',')
    data = data.values.tolist()
    objs = []
    for elt in data:
        o = Objet(*elt)
        objs.append(o) # liste d'objets


    # mesure des temps de calcul pour des poids de sac differents
    C=[4] # 0.6, 2, 3, 4, 5, 6, 7
    times = []

    for val in C:
        mvals = []
        for i in range(3):

            start_time = time.time()

            # best = brute_force_binary(objs, val)
            # best = glouton(objs, val)
            best = branch(objs, val)

            end_time = time.time()
            best.print()
            mvals.append(end_time - start_time)
        times.append(np.mean(mvals))
    print(times)

        #print(f'Temps d\'exécution en secondes pour la fonction : {(end_time - start_time) / 1}; en ms : {(end_time - start_time) * 1000 / 1}')