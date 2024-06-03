import pandas as pd
import time

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

def brute_force(objects_list:list, backpack_size:float):
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


# Fonction pour trouver le maximum de la somme des éléments à l'index [2]
def max_sum_element_n(liste_de_listes, n):
    sommes = []

    for sous_liste in liste_de_listes:
        if sous_liste:  # Vérifier que la sous-liste n'est pas vide
            elements_n = [item[n] for item in sous_liste if len(item) > n]  # Extraire les éléments à l'index n
            somme = sum(elements_n)
            sommes.append(somme)

    if sommes:  # Vérifier que la liste des sommes n'est pas vide
        max_somme = max(sommes)
        print(sommes)
    else:
        max_somme = None  # Retourner None s'il n'y a pas de sommes valides

    return max_somme


def max_sum_element_n_bis(liste_de_listes, n):
    max_somme = None
    max_index = None
    max_sous_liste = None

    for index, sous_liste in enumerate(liste_de_listes):
        if sous_liste:  # Vérifier que la sous-liste n'est pas vide
            elements_n = [item[n] for item in sous_liste if len(item) > n]  # Extraire les éléments à l'index n
            somme = sum(elements_n)
            if max_somme is None or somme > max_somme:
                max_somme = somme
                max_index = index
                max_sous_liste = sous_liste

    return max_somme, max_index, max_sous_liste
# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    data = pd.read_csv("sac2.csv", sep=';', decimal=',')
    data = data.values.tolist()
#    start_time = time.time()
    # for i in range(10000):
    #     algo_concon(data, 0.6)
    # end_time = time.time()
    # print(f'start : {start_time}, ')
    # print(f'Temps d\'exécution en secondes pour 10000 * la fonc: {(end_time-start_time)/1}; en ms : {(end_time-start_time)*1000/1}')# pour avoir une moyenne

    start_time = time.time()
    a = brute_force(data, 0.6)
    print(a)
    print(max_sum_element_n_bis(a, 1))
    end_time = time.time()
    print(f'Temps d\'exécution en secondes pour  * la fonc: {(end_time-start_time)/1}; en ms : {(end_time-start_time)*1000/1}')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
