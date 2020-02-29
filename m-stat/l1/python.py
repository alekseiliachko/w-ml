import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import sys


def countMx(N, data):
	Mx = np.sum(data)/N
	return Mx;

def countD(N, data, Mx):
	D = 0
	for u in data:
		D += (u - Mx) ** 2
	D = D / N
	return D;

def countS(D):
	return np.sqrt(D);

def countK(N, data, Mx, D):
	K = []
	for f in range(1,N+1):
		top = 0
		for i in range(0,N-f-1):
			top += (data[i] - Mx) * (data[i+f] - Mx)
		bot = D * N
		K.append(top / bot)
	return K;

def run1(N, data):
	mx = countMx(N, data)
	d = countD(N, data,mx)
	s = countS(d)
	print(mx, " ",d);
	k = countK(N, data, mx, d)
	plt.plot(k, 'ro', color='blue')
	plt.show()
	return 0;

def run2(N, data):

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

	plt.plot(result, 'ro', color='blue')
	plt.show()

	return 0;

def run3(N, data):

	min = np.min(data)
	max = np.max(data)
	n_steps = int(np.trunc( (max - min) / H))+1

	real = np.zeros(n_steps)

	count = 0;

	for i in range(0,n_steps):
		for x in range(0,N-1):
			if ( (data[x] >= min + i * H) and (data[x] <= min + (i+1) * H) ):
				count+= 1
		real[i] = count

	for x in range(0,n_steps):
		real[x] = (real[x] / N)

	real = np.sort(real)

	plt.plot(real, 'ro', color='blue')
	plt.show()

	return 0;



TASK = int(sys.argv[1])
N = int(str(sys.argv[2]))
H = 1 / float( str(sys.argv[3]))
data = np.random.rand(N)



if (TASK == 1):
    run1(N, data)
elif (TASK == 2):
    run2(N, data)
elif (TASK == 3):
    run3(N, data)
