import math
import random

def f(x):
	return math.sin(x) * math.cos(x) * math.exp(x)

if __name__ == '__main__':
	x = []
	y = []
	for i in range(20):
		a = random.uniform(2.5,7.5)
		b = f(a)
		x.append(a)
		y.append(b)
	print(x)
	print(y)