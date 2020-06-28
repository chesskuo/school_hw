import numpy as np
import matplotlib.pyplot as plt

""" USER CONFIG """
equ_squared_max = 44
output_dir = 'output'
""" USER CONFIG """

def init():
	""" initial all data """
	global xs
	global ys
	global es
	global n
	xs = list()
	ys = list()
	es = list()
	f = open('dataset')
	l = f.readlines()
	n = len(l) - 1
	for i in range(1, n+1):
		tmp = l[i].split()
		xs.append(float(tmp[0]))
		ys.append(float(tmp[1]))
	f.close()

def cal_coeffs(m):
	"""
	return Pm(x) coeffs
	y = a0 + a1*x + a2*x^2 ...
	"""
	global xs
	global ys
	global n
	d = m + 1
	A = np.zeros((d, d))
	B = np.zeros((d, 1))
	# cal A matrix
	for i in range(d):
		for j in range(d):
			for x in xs:
				A[i][j] += pow(x, i+j)
	# cal B matrix
	for i in range(d):
		for j in range(n):
			B[i][0] += ys[j] * pow(xs[j], i)
	return np.linalg.solve(A, B)

def cal_error(cs):
	global xs
	global ys
	global n
	m = len(cs) - 1
	e = 0.0
	for i in range(n):
		tmp = 0.0
		for j in range(m + 1):
			tmp += cs[j][0] * pow(xs[i], j)
		e += pow(ys[i] - tmp, 2)
	e /= (n - m)
	return e

def best_choice():
	"""
	return a tuple
	[0] = best squared val
	[1] = error val
	"""
	global es
	mn_idx = 0
	mn_e = 1e100
	for i in range(len(es)):
		if es[i] < mn_e:
			mn_e = es[i]
			mn_idx = i
	return (mn_idx+1, mn_e)

def format_output(fn, data):
	f = open(f'{output_dir}/{fn}', 'w')
	for i in range(len(data)):
		print(i+1, data[i], file=f)


if __name__ == '__main__':
	init()

	for i in range(1, equ_squared_max+1):
		coeffs = cal_coeffs(i)
		global es
		es.append(cal_error(coeffs))

	format_output('error.txt', es)
	best = best_choice()

	def pm(x):
		coeffs = cal_coeffs(best[0])
		y = 0.0
		for i in range(len(coeffs)):
			y += coeffs[i][0] * pow(x, i)
		return y

	global xs
	global ys
	line_x = np.linspace(0.0, 10.0, 100)
	line_y = [ pm(x) for x in line_x ]

	plt.title(f'The Best Choice is P{best[0]}(x)', fontsize=20)
	plt.xlabel('X')
	plt.ylabel('Y')
	plt.scatter(xs, ys, color='black')
	plt.plot(line_x, line_y, color='red')
	plt.savefig(f'{output_dir}/ls_best.png')