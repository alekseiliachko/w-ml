
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

def RNUNIF(b, a):
    return (b - a) * np.random.random() + a;


def RNRFM1():
    return math.sqrt(-2 * math.log(np.random.random())) * math.cos(2 * math.pi * np.random.random());


def RNRFM2():
    s = 0
    for i in range(0,12):
        s += np.random.random()
    return s - 6;


def RNEXP(b):
    return -b * math.log(np.random.random());


def RNCHIS():
    s = 0
    for i in range(0,10):
        t = RNRFM1()
        s += t ** 2
    return s


def RNSTUD():
    return RNRFM1() / math.sqrt(RNCHIS() / 10)


def plotn(step, end, begin, arr):
    x = begin
    res = []
    while (x <= end - step):
        c = 0
        for i in range(0,N):
            if ( (arr[i] >= x) & (arr[i] < x + step) ):
                c += 1
        x = x + step
        res.append(c / (N * step))

    x = np.linspace(0, 1, num=int((end-begin) / step))
    plt.plot(x, res,  color='blue')
    plt.show()
    
    return 0;



def integral(step, end, start, arr):
    x = start
    c = 0
    res = []
    while (x <= end - step):
        for i in range (0, N):
            if ( (arr[i] >= x) & (arr[i] < x + step) ):
                c += 1
        x = x + step
        res.append(c / N)

    x = np.linspace(0, 1, num=int((end-start)/ step))
    plt.plot(x, res, 'ro', color='blue')
    plt.show()
    
    return 0;


def run1(k):
    arr = []
    for i in range(0,N):
        arr.append(RNUNIF(11, 1))

    print(countMx(arr))
    print(countD(arr))

    if (k == 1):
        plotn(1, 12, 0.0, arr)
    else:
        integral(1, 12, 0.0, arr)
    return 0;

def run2(k):
    arr = []
    for i in range(0,N):
        arr.append(RNRFM1())

    print(countMx(arr))
    print(countD(arr))
    

    if (k == 1):
        plotn(0.5, 4, -4.0, arr)
    else:
        integral(0.5, 4, -4.0, arr)
    return 0;

def run3(k):
    arr = []
    for i in range(0,N):
        arr.append(RNRFM2())

    print(countMx(arr))
    print(countD(arr))
    
    
    if (k == 1):
        plotn(0.5, 4, -4.0, arr)
    else:
        integral(0.5, 4, -4.0, arr)
    return 0;

def run4(k):
    arr = []
    for i in range(0,N):
        arr.append(RNEXP(5))

    print(countMx(arr))
    print(countD(arr))
    

    if (k == 1):
        plotn(1, 50, 0.0, arr)
    else:
        integral(1, 50, 0.0, arr)
    return 0;

def run5(k):
    arr = []
    for i in range(0,N):
        arr.append(RNCHIS())

    print(countMx(arr))
    print(countD(arr))
    

    if (k == 1):  
        plotn(1, 30, 0.0, arr)
    else:
        integral(1, 30, 0.0, arr)
    return 0;

def run6(k):
    arr = []
    for i in range(0,N):
        arr.append(RNSTUD())

    print(countMx(arr))
    print(countD(arr))
    

    if (k == 1):
        plotn(0.5, 6, -6.0, arr)
    else:
        integral(0.5, 6, -6.0, arr)
    return 0;


TASK = int(sys.argv[1])

KEY = int(sys.argv[2])

N = 10000

if   (TASK == 1):
    run1(KEY)
elif (TASK == 2):
    run2(KEY)
elif (TASK == 3):
    run3(KEY)
elif (TASK == 4):
    run4(KEY)
elif (TASK == 5):
    run5(KEY)
elif (TASK == 6):
    run6(KEY)

