def f1(a1,a2,b1,x2):
	return -(a2 * x2 + b1)/ (2 * a1);
def f2(a3,a2,b2,x1):
	return -(a2 * x1 + b2)/ (2 * a3);
import math

def ssin(dx1, dx2):
	a = dx1 
	b = dx2
	c = math.sqrt(a*a + b*b)
	return b / c;
def ccos(dx1, dx2):
	a = dx1
	b = dx2
	c = math.sqrt(a*a + b*b)
	return a / c;

def ch1(x,y,sin,cos,a,b):
	return (-a * cos - b * sin + cos * x + sin * y)

def ch2(x,y,sin,cos,a,b):
	return (a * sin - cos * b + cos * y - sin * x)

def run(x1,x2,a1,a2,a3,b1,b2,N):
	dx = 0
	dy = 0
	a = x1
	b = x2

	for i in range(0,N):
		print("------------")
		a = x1
		b = x2
		x1 = f1(a1,a2,b1,x2)
		x2 = f2(a3,a2,b2,x1)
		print("coord x1 = ", x1)
		print("coord x2 = ", x2)
		dx = abs(x1 - a)
		dy = abs(x2 - b)
		print("dx = ", dx)
		print("dy = ", dy)
		sin = ssin(dx,dy)
		cos = ccos(dx,dy)
		print("sin = ", sin)
		print("cos = ", cos)
		tempx1 = x1
		tempx2 = x2
		x1 = ch1(tempx1,tempx2,sin,cos,a,b)
		x2 = ch2(tempx1,tempx2,sin,cos,a,b)
		print("x1' =", x1)
		print("x2' =", x2)
	return 0;

N = 4

x1 = -2.25
x2 = 2.25
a1 = 125.45
a2 = -148.5
a3 = 46.25
b1 = -6.8
b2 = -6.8

run(x1,x2,a1,a2,a3,b1,b2,N)
