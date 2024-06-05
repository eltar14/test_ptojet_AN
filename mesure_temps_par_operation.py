import time
def mesure_temps(n1=10000, n2 = 10000):
    x = 0
    for i in range(n1):
        for j in range(n2):
            a = i+j
            x += a*j
    return x


if __name__ == '__main__':
    time_start = time.time()
    print(mesure_temps())
    time_end = time.time()

    time_elapsed = time_end-time_start
    time_per_op = time_elapsed/(10000*10000*3)
    print(time_per_op)
    print(time_elapsed, 's pour ', 10000*10000*3, "operations")