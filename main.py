import pandas as pd
import time
import math

class Objet:
    def __init__(self, nom, masse, utilite):
        self.nom = nom
        self.masse = masse
        self.utilite = utilite

    def ratio(self):
        return self.utilite/math.sqrt(self.masse)
    def print(self):
        print(f'{self.nom} ; {self.masse} ; {self.utilite}')


class Bag:
    def __init__(self):
        self.content = [] # contient des Objets
        self.weight = 0
        self.score = 0

    def add(self, obj:Objet):
        self.content.append(obj)
        self.weight += obj.masse
        self.score += obj.utilite

    def print(self):
        print(f'Contenu du sac de masse: {self.weight} et d\'utilite {self.score}')
        for elt in self.content:
            #self.content[i].print()#f'{obj.nom} ; {obj.masse} ; {obj.utilite}'
            elt.print()#f'{obj.nom} ; {obj.masse} ; {obj.utilite}'



    def get_mass(self):
        sum = 0
        for o in self.content:
            sum += o.masse
        return sum

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

def brute_force(objects_list:dict, backpack_size:float):
    #print(objects_list)
    bags = []
    for i in range(2**len(objects_list)-1):
        bag = []
        binaire_sans_prefixe = bin(i)[2:].zfill(len(objects_list))
        #print(binaire_sans_prefixe)
        #print(binaire_sans_prefixe)
        for j in range(len(objects_list)):
            #print(binaire_sans_prefixe[j])
            #print(int(binaire_sans_prefixe[j]) == 1)
            if(int(binaire_sans_prefixe[j]) == 1):
                bag.append(objects_list[j])
                #print(objects_list[j])
        bags.append(bag)
        if(i>1000):
            break
    return bags






def brute_force_avec_Obj(objects_list:list, backpack_size:float):
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



def glouton(objects_list:list, backpack_size:float):
    EPSILON = 0.00001
    sorted_by_ratio = sorted(objects_list, key=lambda k: k.ratio(), reverse=True)
    bag = Bag()
    i = 0
    while((bag.weight + sorted_by_ratio[i].masse) < backpack_size + EPSILON):
        bag.add(sorted_by_ratio[i])
        i+=1
    return bag










def brute_force_demo():
    data = pd.read_csv("sac2.csv", sep=';', decimal=',')
    data = data.values.tolist()
    objs = []
    for elt in data:
        #print(*elt)
        o = Objet(*elt)
        objs.append(o)
    start_time = time.time()
    b = brute_force_avec_Obj(objs, 0.6)
    end_time = time.time()
    print(len(b))
    best = max(b, key=lambda k: k.score)
    best.print()
    print(f'Temps d\'exécution en secondes pour  * la fonc: {(end_time - start_time) / 1}; en ms : {(end_time - start_time) * 1000 / 1}')




if __name__ == '__main__':
    #brute_force_demo()

    data = pd.read_csv("sac2.csv", sep=';', decimal=',')
    data = data.values.tolist()
    objs = []
    for elt in data:
        o = Objet(*elt)
        objs.append(o)
    glouton(objs, 0.6).print()