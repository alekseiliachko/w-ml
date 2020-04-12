import random
import math

def func(T,x):
    return (
        x[0] > T and x[1] > T or x[2] > T and x[3] > T and 
        x[4] > T and 
        x[5] > T and 
        x[6] > T and x[7] > T or x[8] > T and x[9] > T or x[10] > T and x[11] > T 
        ); 
    # return (
    #     (x[0] > T and x[1] > T) or (x[2] > T and x[3] > T) and 
    #     (x[4] > T) and 
    #     (x[5] > T) and 
    #     ( (x[6] > T and x[7] > T) or (x[8] > T and x[9] > T) or (x[10] > T and x[11] > T) ) 
    #     ); 

def work(N, T, L):
    m = 3
    lambdas = [40 * 10 ** -6, 10 * 10 ** -6, 80 * 10 ** -6]
    n = [4,2,6]
    d = 0

    for k in range(0,N):
        x = []

        for i in range(0,m):
            t = []
            for j in range(0,n[i]):
                a = random.random()
                t.append(-math.log(a) / lambdas[i])

            for j in range(0, L[i]):
                l = t.index(min(t))
                t[l] = t[l] - math.log(random.random()/lambdas[i])

            for j in range(0,n[i]):
                x.append(t[j])
        
        if not func(T,x):
            d = d + 1
    
    return 1 - d / N

P0 = 0.999
TT = 8760
L = [0,0,0]

alpha = 99.9
eps = 0.001
tau = 3.090

NN = math.trunc(tau**2 * ( ((1 - P0) * P0) / eps ** 2 ))
print("N = ", NN)

wtb = 0
wtf = 5

for i in range (wtb,wtf):
    L[0] = i

    for j in range(wtb,wtf):
        L[1] = j
        
        for k in range (wtb,wtf):
            
            L[2] = k
            P = work(NN,TT,L)

            # if (P > P0):
            #     print("P = ", P, "L = ", " ", sum(L))
            
            print("P = ", P, "L = ", L, " ", sum(L))
