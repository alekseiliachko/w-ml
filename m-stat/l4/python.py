import random
import math

def func(x):
    T = 8760;
    return 
    ((((x[0] > T) & (x[1] > T)) | ((x[2] > T) & (x[3] > T))) & 
    (x[4] > T) & (x[5] > T) & 
    ( ((x[6] > T) & (x[7] > T)) | ((x[8] > T) & (x[9] > T)) | ((x[10] > T) & (x[11] > T)) )); 


def work(L):
    N = 33012
    m = 3
    lambdas = [40 * 10 ** -6, 10 * 10 ** -6, 80 * 10 ** -6]
    n = [4,2,6]
    d = 0

    for k in range(0,N):
        x = []

        for i in range(0,m):
            t = []
            for j in range(0,n[i]):
                a =random.random()
                t.append(-math.log(a) / lambdas[i])

            for j in range(0, L[i]):
                l = t.index(min(t))
                t[l] = t[l] - math.log(random.random()/lambdas[i])

            for j in range(0,n[i]):
                x.append(t[j])
        
        if not func(x):
            d = d + 1
            # print(d)

    return 1 - (d / N);

P0 = 0.999
L = [0,0,0]

wtb = 5
wtf = 10

for i in range (wtb,wtf):
    L[0] = i

    for j in range(wtb,wtf):
        L[1] = j
        
        for k in range (wtb,wtf):
            
            L[2] = k
            P = work(L)

            # if (P > P0):
            #     print("LOOK ABOVE")
            #     print("P = ", P, "L = ", " ", sum(L))
            
            print("P = ", P, "L = ", " ", sum(L))


