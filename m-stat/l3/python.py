
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import sys
import math


# function RNUNIF(b, a) {
#   return (b - a) * Math.random() + a;
# }

def RNUNIF(b, a):
    return (b - a) * np.random.random() + a;

# function RNRFM1() {
#   return Math.sqrt(-2 * Math.log(Math.random())) * Math.cos(2 * Math.PI * Math.random());
# }


def RNRFM1():
    return math.sqrt(-2 * math.log(np.random.random())) * math.cos(2 * math.pi * np.random.random());

# function RNRFM2() {
#   sum = 0.0
#   for (let i = 0; i < 12; i++)
#     sum += Math.random()
#   return sum - 6
# }



def RNRFM2():
    s = 0
    for i in range(0,12):
        s += np.random.random()
    return s - 6;

# function RNEXP(b) {
#   return -b * Math.log(Math.random());
# }

def RNEXP(b):
    return -b * math.log(np.random.random());


# function RNCHIS() {
#   let sum = 0.0
#   for (let i = 0; i < 10; i++) {
#     let tmp = RNRFM1()
#     sum += tmp ** 2
#   }
#   return sum
# }


def RNCHIS():
    s = 0
    for i in range(0,10):
        t = RNRFM1()
        s += t ** 2
    return s


# function RNSTUD() {
#   return RNRFM1() / Math.sqrt(RNCHIS() / 10);
# }


def RNSTUD():
    return RNRFM1() / math.sqrt(RNCHIS() / 10)


# function createPlotnost(step, end, start, arr) {
#   let x = start;
#   while (x <= end - step) {
#     let count = 0;
#     for (let i = 0; i < 10000; i++) {
#       if (arr[i] >= x && arr[i] < x + step) {
#         count += 1;
#       }
#     }
#     console.log(count / (10000 * step));
#     x += step;
#   }
# }

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

    plt.plot(res, 'ro', color='blue')
    plt.show()
    
    return 0;


# function createIntegral(step, end, start, arr) {
#   let x = start;
#   let count = 0;

#   while (x <= end - step) {
#     for (let i = 0; i < 10000; i++) {
#       if (arr[i] >= x && arr[i] < x + step)
#         count += 1
#     }
#     console.log(count / 10000);
#     x += step;
#   }
# }

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

    plt.plot(res, 'ro', color='blue')
    plt.show()
    
    return 0;


def run1(k):
    arr = []
    for i in range(0,N):
        arr.append(RNUNIF(11, 1))

    if (k == 1):
        plotn(1, 12, 0.0, arr)
    else:
        integral(1, 12, 0.0, arr)
    return 0;

def run2(k):
    arr = []
    for i in range(0,N):
        arr.append(RNRFM1())

    if (k == 1):
        plotn(0.5, 4, -4.0, arr)
    else:
        integral(0.5, 4, -4.0, arr)
    return 0;

def run3(k):
    arr = []
    for i in range(0,N):
        arr.append(RNRFM2())
    
    if (k == 1):
        plotn(0.5, 4, -4.0, arr)
    else:
        integral(0.5, 4, -4.0, arr)
    return 0;

def run4(k):
    arr = []
    for i in range(0,N):
        arr.append(RNEXP(5))

    if (k == 1):
        plotn(1, 50, 0.0, arr)
    else:
        integral(1, 50, 0.0, arr)
    return 0;

def run5(k):
    arr = []
    for i in range(0,N):
        arr.append(RNCHIS())

    if (k == 1):  
        plotn(1, 30, 0.0, arr)
    else:
        integral(1, 30, 0.0, arr)
    return 0;

def run6(k):
    arr = []
    for i in range(0,N):
        arr.append(RNSTUD())

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


# let a = 3;
# let N = 10000
# let arr = []
# if (a == 0) {
#   for (let i = 0; i < N; i++) {
#     arr.push(RNUNIF(11, 1))
#   }
#   createPlotnost(1, 12, 0.0, arr)
#   console.log("***")
#   createIntegral(1, 12, 0.0, arr)
# }

# if (a == 1) {
#   for (let i = 0; i < N; i++) {
#     arr.push(RNRFM1())
#   }
#   createPlotnost(0.5, 4, -4.0, arr)
#   console.log("***")
#   createIntegral(0.5, 4, -4.0, arr)
# }

# if (a == 2) {
#   for (let i = 0; i < N; i++) {
#     arr.push(RNRFM2());
#   }
#   createPlotnost(0.5, 4, -4.0, arr)
#   console.log("***")
#   createIntegral(0.5, 4, -4.0, arr)
# }

# if (a == 3) {
#   for (let i = 0; i < N; i++) {
#     arr.push(RNEXP(5))
#   }
#   createPlotnost(1, 50, 0.0, arr)
#   console.log("***")
#   createIntegral(1, 50, 0.0, arr)
# }

# if (a == 4) {
#   for (let i = 0; i < N; i++)
#     arr.push(RNCHIS())
#   createPlotnost(1, 30, 0.0, arr)
#   console.log("***")
#   createIntegral(1, 30, 0.0, arr)
# }

# if (a == 5) {
#   for (let i = 0; i < N; i++)
#     arr.push(RNSTUD())
#   createPlotnost(0.5, 6, -6.0, arr)
#   console.log("***")
#   createIntegral(0.5, 6, -6.0, arr)
# }





#  console.log(mean(arr))
#  console.log(var(arr))



#отчет