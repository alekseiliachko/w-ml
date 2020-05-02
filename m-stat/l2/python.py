
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import sys
import math




# function gaussrand(MO, sko) {
#   sum = 0;
#   for (let i = 0; i < 28; i++)
#     sum += 1.0 * rand() / RAND_MAX;
#   return (sqrt(2.0) * (sko) * (sum - 14.)) / 2.11233 + MO;
# }

def gaussR(M0, sko):
    s = 0
    for i in range(0,28):
        s = s + 1 * np.random.random() / 25699
    return (math.sqrt(2) * sko * (s - 14)) / 2.11233 + M0


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
    def _mx(N,p):
        return(N*p);
    def _d(N,p):
        return(N*p*(1-p))
    def _s(D):
        return np.sqrt(D)
    def gaussR(m,s):
        sum = 0
        for i in range(0,28):
            sum += 1.0 * np.random.rand() / 32767;
        return ( np.sqrt(2.0) * s + (sum - 14) / 2.11233 + m );
    def RNNORM(n,p):
        if (n > 100):
            m = _mx(N,p)
            d = _d(N,p)
            s = _s(d)
            return np.round(gaussR(  m, s ))
        else:
            temp = np.random.rand()
            p_ = (1 - p) ** n
            count = 0

            while(temp - p_ >= 0):
                temp = temp - p_
                p_ = p_ * ( ((n - count)/(count + 1))*(p/(1 - p)) )
                count += 1
            return count

    array = np.zeros(N);
    for i in range(0,N-1):
        array[i] = RNNORM(10,p)
    return array;

def fillGR1(N,p):
    def IRNGEO1(p):
        temp = np.random.rand()
        p_ = p
        count = 0
        while(temp - p_):
            temp = temp - p_
            p_ = p_ * (1 - p_)
            count += 1
        return count;

    array = np.zeros(N);
    for i in range(0,N-1):
        array[i] = IRNGEO1(p)
    return array;

def fillGR2(N,p):
    def IRNGEO2(p):
        temp = np.random.rand()
        count = 0
        while(temp > p):
            temp = np.random.rand()
            count+= 1
        return count;

    array = np.zeros(N);
    for i in range(0,N-1):
        array[i] = IRNGEO2(p)
    return array;

def fillGR3(N,p):
    def IRNGEO3(p):
        temp = np.random.rand()
        return np.round(math.log(temp) / math.log(1 - p)) + 1;
    array = np.zeros(N);
    for i in range(0,N-1):
        array[i] = IRNGEO3(p)
    return array;

def fillPR1(N,mu):
    def IRNPOI(mu):
        if (mu < 88):
            temp = np.random.random()
            p_ = math.exp(-mu)
            count = 1
            while (temp - p_ >= 0):
                temp = temp - p_
                p_ = p_ * mu / count
                count = count + 1
            return count;
        else:
            return gaussR(mu, mu);
    array = np.zeros(N);
    for i in range(0,N-1):
        array[i] = IRNPOI(mu)
    return array;

def fillPR2(N,mu):
    def IRNPSN(mu):
        if (mu < 88):
            temp = np.random.rand();
            p_ = temp;
            count = 1;
            while (p_ >= np.exp(-mu)):
                temp = np.random.random()
                p_ = p_ * temp;
                count= count + 1;
            return count;
        else:
            return gaussR(mu, mu);
    array = np.zeros(N);
    for i in range(0,N-1):
        array[i] = IRNPSN(mu)
    return array;

def fillLR(N,mu):
    def IRNLOG(q):
        temp = np.random.rand();
        p_ = -(1 * 1.0 / np.log(q)) * (1 - q);
        count = 1;
        while (temp - p_ >= 0):
            temp = temp - p_
            p_ = p_ * ((count * 1.0 / (count + 1)) * (1 - q))
            count= count + 1
        return count;
    array = np.zeros(N);
    for i in range(0,N-1):
        array[i] = IRNLOG(mu)
    return array;

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

N = 10000
H = 0.5

if (TASK == 1):
    data = fillRR(N,1,100)
    print(data)
elif (TASK == 2):
    data = fillBR(N,0.5)
    print(data)
elif (TASK == 3):
    data = fillGR1(N,0.5)
    print(data)
elif (TASK == 4):
    data = fillGR2(N,0.5)
    print(data)
elif (TASK == 5):
    data = fillGR3(N,0.5)
    print(data)
elif (TASK == 6):
    data = fillPR1(N,10)
    print(data)
elif (TASK == 7):
    data = fillPR2(N,10)
    print(data)
elif (TASK == 8):
    data = fillLR(N,0.5)
    print(data)

print(countMx(data))
print(countD(data))


min = np.min(data)
max = np.max(data)
n_steps = int(np.trunc( (max - min) / H))+1

plt.subplot(2, 1, 1)
x = np.linspace(0, 1, n_steps)
plt.plot(x, countP(data)/20, color='blue')
plt.subplot(2, 1, 2)
plt.plot(x, countI(data)/2, 'ro', color='blue')
plt.show()

#отчет