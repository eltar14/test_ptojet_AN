import pandas as pd
import time
import math
from Objet import Objet
from Bag import Bag
from BinaryTree import BinaryTree




def algo_concon(objects_list:list, backpack_size:float): # 19 op
    sac = []
    #print(objects_list)
    p = 0
    i=0
    while(p+objects_list[i][1]<backpack_size):# 2 op
        sac.append(objects_list[i][0]) # 1op
        p+= objects_list[i][1] # 1 op
        i+=1 # 1 op

    #print(f'Elements dans le sac : {sac}\nPoids : {p}')

# def brute_force(objects_list:dict, backpack_size:float):
#     """
#     pas utilisé !
#     :param objects_list:
#     :param backpack_size:
#     :return:
#     """
#     #print(objects_list)
#     bags = []
#     for i in range(2**len(objects_list)-1):
#         bag = []
#         binaire_sans_prefixe = bin(i)[2:].zfill(len(objects_list))
#         #print(binaire_sans_prefixe)
#         #print(binaire_sans_prefixe)
#         for j in range(len(objects_list)):
#             #print(binaire_sans_prefixe[j])
#             #print(int(binaire_sans_prefixe[j]) == 1)
#             if(int(binaire_sans_prefixe[j]) == 1):
#                 bag.append(objects_list[j])
#                 #print(objects_list[j])
#         bags.append(bag)
#         if(i>1000):
#             break
#     return bags






def brute_force_avec_Obj_aux(objects_list:list, backpack_size:float):
    bags = []
    for i in range(2**len(objects_list)-1):
        bag = Bag()
        binaire_sans_prefixe = bin(i)[2:].zfill(len(objects_list))
        for j in range(len(objects_list)):
            if(int(binaire_sans_prefixe[j]) == 1):
                bag.add(objects_list[j])
        if(bag.weight <= (backpack_size+0.005)): # +epsilon pour l'erreur de float de python
            bags.append(bag)
    return bags

def brute_force(objects_list:list, backpack_size:float):
    return max(brute_force_avec_Obj_aux(objects_list, backpack_size), key=lambda k: k.score)

def glouton(objects_list:list, backpack_size:float):
    EPSILON = 0.00001
    sorted_by_ratio = sorted(objects_list, key=lambda k: k.ratio(), reverse=True)
    bag = Bag()
    i = 0
    while((bag.weight + sorted_by_ratio[i].masse) < backpack_size + EPSILON):
        bag.add(sorted_by_ratio[i])
        i+=1
    return bag

def branch(objects_list:list, backpack_size:float):
    root = BinaryTree(0)
    root.create_tree(objs, 0.6)
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



    start_time = time.time()

    #best = brute_force(objs, 0.6)
    # best = glouton(objs, 0.6)
    best = branch(objs, 0.6)

    end_time = time.time()
    best.print()
    print(f'Temps d\'exécution en secondes pour la fonction : {(end_time - start_time) / 1}; en ms : {(end_time - start_time) * 1000 / 1}')



    # Branch and Bound avec arbre binaire
    from BinaryTree import BinaryTree
    ab = BinaryTree(0) # valeur score de zero car debut # a gauche les oui a droite les non


