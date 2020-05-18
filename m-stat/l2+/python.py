import scipy.stats
import numpy as np
import enum
import math

# const { jStat } = require('jstat');
# // Пуассон

# function IRNPOI(mu = 10) {
#  if (mu < 88) {
#  let a = Math.random();
#  let p_t = Math.exp(-mu);
#  let m = 1;
#  while (a - p_t >= 0) {
#  a -= p_t;
#  p_t *= mu;
#  m++;
#  }
#  return m;
#  } else {
#  return gauss(mu);
#  }
# }

def IRNGEO1(p):
    p_intervals = p
    M = np.random.uniform()
    m = 1
    while (M >= p_intervals):
        M -= p_intervals
        p_intervals *= (1-p)
        m += 1
    return m

def IRNGEO2(p):
    temp = np.random.rand()
    count = 1
    while(temp > p):
      temp = np.random.rand()
      count += 1
    return count;


def IRNGEO3(p):
    return math.floor(math.log(np.random.uniform()) / math.log(1 - p)) + 1

def Geom(n, p):
    return 1 - (1-p) ** (n);



arr = []
amout = []
N = 1000
x = 0.0

for i in range(0,N):
    arr.append(IRNGEO3(0.5));

while (x < 26):
    c = 0
    for i in range(0,N):
        if (arr[i] >= x) and (arr[i] < x + 1.0):
            c = c + 1
    amout.append(c)

    x = x + 1.0

sum = 0.0

for i in range(1, 26):
    pi = Geom(i,0.5) - Geom(i-1,0.5)
    if (pi != 0):
        sum = sum + pow(amout[i] - N * pi, 2) / (N * pi);

print(sum / 1000);