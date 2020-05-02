import scipy.stats
import numpy as np
import enum
import math

def rb(tmp, s):
    n = len(tmp) - len(s)
    index = len(tmp) - 1
    if len(s) >= len(tmp):
        s[index] = s[index] + 1
    else:
        for i in range(n):
            s = np.append(s, 0)
        s[index] += 1
    tmp.clear()
    return s


def check(x, d):
	v = np.array([], int)
	tmp = []
	for number in x:
		if len(tmp) == 0:
			tmp.append(number)
		elif (tmp[-1] >= number and d == 0) or (
			tmp[-1] <= number and d == 1):
			tmp.append(number)
		else:
			v = rb(tmp, v)
	if len(tmp) != 0:
		v = rb(tmp, v)
	sum_v = np.sum(v)
	p = []
	for i in range (1, len(v) + 1):
		p.append((1 / math.factorial(i))-(1 / math.factorial(i + 1)))
	chisquare = 0
	for i in range (0, len(v)):
		chisquare += ((v[i]-sum_v*p[i])**2)/(sum_v*p[i])
	return chisquare

n = 10000
x = np.random.uniform(0, 1, n)
print('Хи^2 Невозрастания', check(x, 0))
print('Хи^2 Неубывания', check(x, 1))