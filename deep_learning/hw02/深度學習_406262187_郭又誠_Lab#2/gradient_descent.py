import numpy as np

np.seterr(all='ignore')

class GDA(object):
	""" Gradient Descent Algorithm """
	def __init__(self, d, eta=1.0, epoch=100000):
		np.random.seed()
		self.eta = eta
		self.epoch = epoch
		self.w = np.random.uniform(-3, 3, d+1)
		self.w_init = self.w

	def train(self, data):
		x, t = self._parseData(data, True)
		ep = 0
		while ep <= self.epoch:
			for i in range(len(t)):
				y_hat = self._sigmoid(self.w.dot(x[i].T))
				if self._cross_entropy(t[i], y_hat) < 0.01:
					print('w_init:', self.w_init)
					print('w:', self.w)
					print('epoch:', ep)
					return
				self.w = self.w + self.eta * (t[i] - y_hat) * x[i]
			ep += 1
		print('w_init:', self.w_init)
		print('w:', self.w)
		print('epoch:', ep)

	def test(self, data):
		x = self._parseData(data)
		t = []
		for i in range(len(x)):
			tmp = self._sigmoid(self.w.dot(x[i].T))
			t.append(1 if tmp >= 0.5 else 0)
		return t

	def _parseData(self, d, have_t=False):
		x = []
		t = []
		for i in range(len(d)):
			x.append([1., float(d[i][0]), float(d[i][1])])
			if have_t:
				t.append(d[i][2])
		if have_t:
			return np.array(x), np.array(t)
		else:
			return np.array(x)

	def _sigmoid(self, t):
		return 1. / (1. + np.exp(-t))

	def _cross_entropy(self, y, y_hat):
		return -(y * np.log(y_hat) + (1. - y) * np.log(1. - y_hat))