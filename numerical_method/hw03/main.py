import numpy as np
from scipy.interpolate import lagrange
from numpy.polynomial.polynomial import Polynomial
import matplotlib.pyplot as plt





def Lagrange(x, y, dataset):
	""" Lagrange """
	poly = lagrange(x, y)
	c = Polynomial(poly).coef.tolist()
	c.reverse()

	lineX = []
	lineY = []
	a = 0
	b = 10
	while a <= b:
		value = a;
		sum = 0;
		for i in range(0, len(c)):
			sum = sum + c[i] * pow(value, i)
		lineX.append(value)
		lineY.append(sum)
		a += 0.001
	plt.cla()
	plt.clf()
	plt.title(str(dataset) + "Lagrange")
	ORI, = plt.plot(x,y,'bo')
	RES, = plt.plot(lineX,lineY,'r:')
	plt.savefig("./out/" + str(dataset) + "-Lagrange.png")





def NDD(x, y, dataset):
	""" Newton Divided Difference """
	n = np.shape(y)[0]
	pyramid = np.zeros([n, n])
	pyramid[::,0] = y
	for j in range(1,n):
		for i in range(n-j):
			pyramid[i][j] = (pyramid[i+1][j-1] - pyramid[i][j-1]) / (x[i+j] - x[i])
	coeff_vector = pyramid[0]
	final_pol = np.polynomial.Polynomial([0.])
	n = coeff_vector.shape[0]
	for i in range(n):
		p = np.polynomial.Polynomial([1.])
		for j in range(i):
			p_temp = np.polynomial.Polynomial([-x[j], 1.])
			p = np.polymul(p, p_temp)
		p *= coeff_vector[i]
		final_pol = np.polyadd(final_pol, p)
	c = np.flip(final_pol[0].coef, axis=0).tolist()
	c.reverse()
	
	lineX = []
	lineY = []
	a = 0
	b = 10
	while a <= b:
		value = a;
		sum = 0;
		for i in range(0, len(c)):
			sum = sum + c[i] * pow(value, i)
		lineX.append(value)
		lineY.append(sum)
		a += 0.001
	plt.cla()
	plt.clf()
	plt.title(str(dataset) + "NDD")
	ORI, = plt.plot(x,y,'bo')
	RES, = plt.plot(lineX,lineY,'r:')
	plt.savefig("./out/" + str(dataset) + "-NDD.png")





def u_cal_f(u, n):
	temp = u;
	for i in range(1, n):
		temp = temp * (u - i);
	return temp;

def fact_f(n):
	f = 1;
	for i in range(2, n + 1):
		f *= i;
	return f;

def GNFD(x, _y, dataset):
	""" Gregory-Newton Forward Difference """
	n = x.size;
	x = x.tolist();
	y = [[0 for i in range(n)]
			for j in range(n)];
	for i in range(n):
		y[i][0] = _y[i]
	for i in range(1, n):
		for j in range(n - i):
			y[j][i] = y[j + 1][i - 1] - y[j][i - 1];
	# for i in range(n):
	# 	print(x[i], end = "\t");
	# 	for j in range(n - i):
	# 		print(y[i][j], end = "\t");
	# 	print("");
	lineX = []
	lineY = []
	a = 0
	b = 10
	while a <= b:
		value = a;
		sum = y[0][0];
		u = (value - x[0]) / (x[1] - x[0]);
		for i in range(1,n):
			sum = sum + (u_cal_f(u, i) * y[0][i]) / fact_f(i);
		lineX.append(value)
		lineY.append(sum)
		a += 0.001
	plt.cla()
	plt.clf()
	plt.title(str(dataset) + "GNFD")
	ORI, = plt.plot(x,_y,'bo')
	RES, = plt.plot(lineX,lineY,'r:')
	plt.savefig("./out/" + str(dataset) + "-GNFD.png")






def u_cal_b(u, n):
	temp = u;
	for i in range(1, n):
		temp = temp * (u - i);
	return temp;

def fact_b(n):
	f = 1;
	for i in range(2, n + 1):
		f *= i;
	return f;

def GNBD(x, _y, dataset):
	""" Gregory-Newton Forward Difference """
	n = x.size;
	x = x.tolist();
	y = [[0 for i in range(n)]
			for j in range(n)]
	for i in range(n):
		y[i][0] = _y[i]
	for i in range(1, n):
		for j in range(n-1, i-1, -1):
			y[j][i] = y[j][i - 1] - y[j - 1][i - 1]
	# for i in range(n):
	# 	for j in range(i+1):
	# 		print(y[i][j], end = "\t")
	# 	print("");
	lineX = []
	lineY = []
	a = 0
	b = 10
	while a <= b:
		value = a;
		sum = y[n - 1][0];
		u = (value - x[n - 1]) / (x[1] - x[0])
		for i in range(1,n):
			sum = sum + (u_cal_b(u, i) * y[n - 1][i]) / fact_b(i)
		lineX.append(value)
		lineY.append(sum)
		a += 0.001
	plt.cla()
	plt.clf()
	plt.title(str(dataset) + "GNBD")
	ORI, = plt.plot(x,_y,'bo')
	RES, = plt.plot(lineX,lineY,'r:')
	plt.savefig("./out/" + str(dataset) + "-GNBD.png")










if __name__ == '__main__':

	x1 = np.array([2.40, 2.75, 2.91, 3.33, 3.89, 3.94, 4.42, 4.65, 4.87, 5.00, 5.33, 5.96, 6.14, 6.53, 6.85, 7.14, 7.35, 7.67, 7.70, 8.10])
	y1 = np.array([-2.5065,-1.4261,0.6374,1.9569,-1.2967,0.0134,-1.7892,-3.6020,4.0695,4.1644,-4.6471,-4.5018,5.5824,-3.6274,-1.5766,5.3962,-3.8348,7.2730,5.6132,7.4893])

	x2 = np.array([2.4,2.7,3.0,3.3,3.6,3.9,4.2,4.5,4.8,5.1,5.4,5.7,6.0,6.3,6.6,6.9,7.2,7.5,7.8,8.1])
	y2 = np.array([-2.5065,-1.9135,1.8316,2.3425,-2.9735,-1.0456,3.9669,-3.9166,1.8038,0.3963,-1.9792,2.6447,-2.4312,1.0453,1.6986,-5.2736,7.1707,-3.6987,-4.6149,7.4893])

	x3 = np.array([4.301939058599446, 4.809224900576026, 3.2311349659099884, 7.209800579165677, 4.055621658516113, 6.121385262851772, 7.458175051207697, 4.3482468854857705, 6.171701615275104, 5.249115211830899, 2.849901404905901, 3.528444772941527, 3.664271165793668, 2.781091172222307, 3.375185216278755, 6.961384699123714, 5.803749832782277, 3.368120987747776, 6.1177279130824225, 7.098173653256061])
	y3 = np.array([27.017597311799758, -11.801519860904014, 2.254075747313046, 649.5157181567994, 27.910726980469924, -72.41960845117889, 616.8530427976903, 25.73928452931376, -52.95937652353829, -83.66579806389369, -4.761018992772735, 11.904211568675809, 16.881495148766945, -5.326200766765138, 6.582160098554637, 515.4684513081397, -135.69014358801041, 6.352119395177021, -73.72695759539396, 603.8188838149387])
	# testx = np.array([45, 50, 55, 60])
	# testy = np.array([0.7071, 0.7660, 0.8192, 0.8660])
	# testx = np.array([1891, 1901, 1911,1921, 1931])
	# testy = np.array([46,66,81,93,101])

	Lagrange(x1, y1, 1)
	NDD(x1, y1, 1)
	GNFD(x1, y1, 1)
	GNBD(x1, y1, 1)

	Lagrange(x2, y2, 2)
	NDD(x2, y2, 2)
	GNFD(x2, y2, 2)
	GNBD(x2, y2, 2)

	Lagrange(x1, y1, 3)
	NDD(x3, y3, 3)
	GNFD(x3, y3, 3)
	GNBD(x3, y3, 3)