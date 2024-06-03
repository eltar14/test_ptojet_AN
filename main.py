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
    return bags



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
    brute_force(data, 0.6)
    end_time = time.time()
    print(f'Temps d\'exécution en secondes pour  * la fonc: {(end_time-start_time)/1}; en ms : {(end_time-start_time)*1000/1}')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
