import numpy as np
import matplotlib.pyplot as plt

class PLA(object):
	""" Perceptron Learning Algorithm """
	d_train = None
	d_test = None
	w = None
	rate = 1

	def __init__(self, rate=1):
		self.rate = rate

	def train(self, fn):
		self.d_train = self._read_data(fn, 3)
		w = np.zeros(2)
		while True:
			r = self._err_check(w)
			if r == None:
				self.w = w
				print('w = ', self.w)
				break
			w = w + self.rate * r[0] * r[1]

	def test(self, fn):
		self.d_test = self._read_data(fn, 2)
		r = []
		for x in self.d_test:
			x = np.array(x)
			r.append(np.sign(self.w.T.dot(x)))
		return tuple(r)

	def _err_check(self, w):
		r = None
		for x, t in self.d_train:
			x = np.array(x)
			if np.sign(w.T.dot(x)) != t:
				return (x, t)
		return r

	def _read_data(self, fn, n):
		with open(fn, 'r') as f:
			tmp = []
			if n == 3:
				for line in f.readlines():
					x, y, t = line.strip().split(',')
					tmp.append(((int(x), int(y)), int(t)))
			elif n == 2:
				for line in f.readlines():
					x, y = line.strip().split(',')
					tmp.append((int(x), int(y)))
			return tuple(tmp)

if __name__ == '__main__':
	pla = PLA()
	pla.train('train.txt')
	r = pla.test('test.txt')
	a = []
	b = []
	aa = []
	bb = []
	# gen points
	for x, t in zip(pla.d_test, r):
		if t == 1:
			a.append(x)
		elif t == -1:
			b.append(x)

	for x, t in pla.d_train:
		if t == 1:
			aa.append(x)
		elif t == -1:
			bb.append(x)
	# draw pic
	p_test_b = plt.scatter([x[0] for x in a], [x[1] for x in a], marker="^", c="black")
	p_test_r = plt.scatter([x[0] for x in b], [x[1] for x in b], marker="^", c="red")
	p_train_b = plt.scatter([x[0] for x in aa], [x[1] for x in aa], c="black")
	p_train_r = plt.scatter([x[0] for x in bb], [x[1] for x in bb], marker="x", c="red")
	plt.plot([-20, 20], [-pla.w[0] * -20 / pla.w[1], -pla.w[0] * 20 / pla.w[1]])
	plt.legend([p_test_b, p_test_r, p_train_b, p_train_r], ['test 1', 'test -1', 'Train 1', 'Train -1'], loc='lower right', shadow=True)
	plt.title('w = ' + str(pla.w))
	plt.xlabel('x')
	plt.ylabel('y', rotation='horizontal')
	plt.show()
