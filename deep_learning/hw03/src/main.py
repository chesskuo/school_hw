from PIL import Image
import os
import numpy as np
import pandas as pd
from sklearn.preprocessing import OneHotEncoder

np.seterr(all='ignore')

def binToJPG(fn):
	if not os.path.exists(f'{fn}/'):
		os.mkdir(f'{fn}/')
	else:
		return

	with open(f'../{fn}.txt', 'r') as f:
		ls = f.readlines()

	for i in range(len(ls)):
		l = ls[i].strip().split(',')
		l = bytes([ int(j) for j in l ])
		img = Image.frombytes('L', (28, 28), l)
		img.save(f'{fn}/' + f'{i:0>4d}.jpg')

def readData():
	img = pd.read_table('../train_img.txt', header=None, dtype=np.float64, sep=',').to_numpy()
	img_label = pd.read_table('../train_label.txt', header=None, sep=',').to_numpy()
	test_img = pd.read_table('../test_img.txt', header=None, sep=',').to_numpy()
	train_label, valid_label = OneHotEncoder().fit_transform(img_label[ : 6400, : ]).toarray(), img_label[ 6400 : , : ]

	data = []
	for i in range(len(img)):
		data.append(img[i].reshape(784, 1))
	data = np.array(data)
	label = []
	for i in range(len(train_label)):
		label.append(train_label[i].reshape(3, 1))
	label = np.array(label)
	test = []
	for i in range(len(test_img)):
		test.append(test_img[i].reshape(784, 1))
	test = np.array(test)

	train_img, valid_img = data[ : 6400, : ], data[ 6400 : , : ]
	train_label = label
	train_data = []
	test_data = []
	for i in range(len(train_img)):
		tmp = (train_img[i], train_label[i])
		train_data.append(tmp)
	for i in range(len(valid_img)):
		tmp = (valid_img[i], valid_label[i])
		test_data.append(tmp)

	return train_data, test_data, test

class Network(object):

	def __init__(self, sizes):
		self.num_layers = len(sizes)
		self.sizes = sizes
		self.biases = [np.random.randn(y, 1) for y in sizes[1:]]
		self.weights = [np.random.randn(y, x) for x, y in zip(sizes[:-1], sizes[1:])]

	def feedforward(self, a):
		for b, w in zip(self.biases, self.weights):
			a = sigmoid(np.dot(w, a) + b)
		return a

	def train(self, training_data, epochs, mini_batch_size, lr, test_data=None):
		training_data = list(training_data)
		n = len(training_data)
		if test_data:
			test_data = list(test_data)
			n_test = len(test_data)

		for j in range(epochs):
			train_accuracy = self._traincheck(training_data) / n
			if train_accuracy > 0.92:
				break
			mini_batches = [ training_data[ k : k + mini_batch_size ] for k in range(0, n, mini_batch_size) ]
			for mini_batch in mini_batches:
				self._update_mini_batch(mini_batch, lr)
			if test_data:
				print(f"Epoch {j}; train accuracy : {train_accuracy} ; test accuracy : {self._evaluate(test_data) / n_test}");
			else:
				print(f"Epoch {j} complete")

	def predict(self, test):
		with open('test.txt', 'w') as f:
			for i in range(len(test)):
				print( np.argmax(self.feedforward(test[i])), file=f)

	def _update_mini_batch(self, mini_batch, lr):
		nabla_b = [ np.zeros(b.shape) for b in self.biases ]
		nabla_w = [ np.zeros(w.shape) for w in self.weights ]
		for x, y in mini_batch:
			delta_nabla_b, delta_nabla_w = self._backprop(x, y)
			nabla_b = [ nb + dnb for nb, dnb in zip(nabla_b, delta_nabla_b) ]
			nabla_w = [ nw + dnw for nw, dnw in zip(nabla_w, delta_nabla_w) ]
		self.weights = [ w - (lr / len(mini_batch) ) * nw for w, nw in zip(self.weights, nabla_w) ]
		self.biases = [ b - (lr / len(mini_batch)) * nb for b, nb in zip(self.biases, nabla_b) ]

	def _backprop(self, x, y):
		nabla_b = [ np.zeros(b.shape) for b in self.biases ]
		nabla_w = [ np.zeros(w.shape) for w in self.weights ]
		# feedforward
		activation = x
		activations = [x]
		zs = []
		for b, w in zip(self.biases, self.weights):
			z = np.dot(w, activation)+b
			zs.append(z)
			activation = sigmoid(z)
			activations.append(activation)
		# backward pass
		delta = self._cost_derivative(activations[-1], y) * sigmoid_prime(zs[-1])
		nabla_b[-1] = delta
		nabla_w[-1] = np.dot(delta, activations[-2].transpose())

		for l in range(2, self.num_layers):
			z = zs[-l]
			sp = sigmoid_prime(z)
			delta = np.dot(self.weights[-l + 1].transpose(), delta) * sp
			nabla_b[-l] = delta
			nabla_w[-l] = np.dot(delta, activations[-l-1].transpose())
		return (nabla_b, nabla_w)

	def _evaluate(self, test_data):
		test_results = [ (np.argmax(self.feedforward(x)), y) for (x, y) in test_data ]

		return sum( int(x == y) for (x, y) in test_results )
	
	def _traincheck(self, train_data):
		train_results = [ ( np.argmax(self.feedforward(x)), np.argmax(y) ) for (x, y) in train_data ]
	
		return sum( int(x == y) for (x, y) in train_results )

	def _cost_derivative(self, output_activations, y):
		return ( output_activations - y )

def sigmoid(x):
	return 1.0 / (1.0 + np.exp(-x))

def sigmoid_prime(x):
	return sigmoid(x) * (1-sigmoid(x))

if __name__ == '__main__':
	binToJPG('train_img')
	binToJPG('test_img')
	layers = [784, 10, 3]
	lr = 0.01
	ep = 10000
	batch_size = 10
	train_data, test_data, test = readData()
	print("\n----- Details Start -----\n")
	print("  Training : 6400")
	print("  Testing : 1600")
	print("  Hidden Layers : 1 layer / 10 neuros")
	print("  Learning Rate : 0.01")
	print("  Epochs : 10000 (max)")
	print("\n----- Details End -----\n")
	model = Network(layers)
	model.train(train_data, ep, batch_size, lr, test_data)
	model.predict(test)
