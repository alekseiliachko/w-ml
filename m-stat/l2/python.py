
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import sys
import math

def countMx(data):
    N = np.size(data)
    Mx = np.sum(data)/N
    return Mx;

def countD(data):
    Mx = countMx(data)
    N = np.size(data)
    D = 0
    for u in data:
        D += (u - Mx) ** 2
    D = D / N
    return D;

def countS(data):
	return np.sqrt(countD(data));

def fillRR(N, min, max):
    array = np.random.rand(N)
    for i in range(0,N-1):
        array[i] = (max - min + 1) * array[i] + min
    return array;

def fillBR(N,p):
    # def countC(n, p):
    #     return math.factorial(n)/(math.factorial(p) * math.factorial(n-p));
    def gaussR(N,p):
        m = N * p
        s = np.sqrt(N * p * (1.0 - p))
        sum = 0
        for i in range(0,28):
            sum += 1.0 * np.random.rand() / 32767;
        return (np.sqrt(2.0) * (s) * (sum - 14)) / 2.11233 + m;
    array = np.zeros(N)
    array[0] = (1 - p) ** N
    for i in range(1,N-1):
        if (i < 90):
            array[i] = array[i -1] * ( ((N - i)/(i + 1))*(p/(1 - p)) )
        else:
            array[i] = np.round(gaussR(N,p) + 0.5)
    return array;

def fillGR1():

    return 0;

def fillGR2():

    return 0;

def fillGR3():

    return 0;

def fillPR1():

    return 0;

def fillPR2():

    return 0;

def fillLR():

    return 0;

def countP(data):
    N = np.size(data)
    min = np.min(data)
    max = np.max(data)
    n_steps = int(np.trunc( (max - min) / H))+1
    estimated = np.full(n_steps,1/(n_steps))
    real = np.zeros(n_steps)
    result = real
    for i in range(0,n_steps):
        for x in range(0,N-1):
            if ( (data[x] >= min + i * H) and (data[x] <= min + (i+1) * H) ):
                real[i] += 1
    for x in range(0,n_steps):
        result[x] = (real[x] / N) / estimated[x]
    return result;

def countI(data):
    N = np.size(data)
    min = np.min(data)
    max = np.max(data)
    n_steps = int(np.trunc( (max - min) / H))+1
    real = np.zeros(n_steps)
    count = 0
    for i in range(0,n_steps):
        for x in range(0,N-1):
            if ( (data[x] >= min + i * H) and (data[x] <= min + (i+1) * H) ):
                count+= 1
        real[i] = count
    for x in range(0,n_steps):
        real[x] = (real[x] / N)
    real = np.sort(real)
    return real;



TASK = int(sys.argv[1])
N = int(str(sys.argv[2]))
H = 1 / float( str(sys.argv[3]))

# data = np.random.rand(N)

if (TASK == 1):
    data = fillRR(N,1,100)
    # data = np.random.rand(N);
elif (TASK == 2):
    data = fillBR(N,0.5)
    print(data)
elif (TASK == 3):
    data = fillGR1()
elif (TASK == 4):
    data = fillGR2()
elif (TASK == 5):
    data = fillGR3()
elif (TASK == 6):
    data = fillPR1()
elif (TASK == 7):
    data = fillGR2()
elif (TASK == 7):
    data = fillLR()

print(countMx(data))
print(countD(data))
plt.subplot(2, 1, 1)
plt.plot(countP(data), color='blue')
plt.subplot(2, 1, 2)
plt.plot(countI(data), 'ro', color='blue')
plt.show()