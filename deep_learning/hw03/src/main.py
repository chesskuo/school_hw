from PIL import Image
import os
import numpy as np
import pandas as pd
from sklearn.preprocessing import OneHotEncoder

def binToJPG(fn):
	if not os.path.exists(f'{fn}/'):
		os.mkdir(f'{fn}/')

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

	# reshape
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

	# cut data to train and test
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
		"""
		The list 'sizes' contains the number of neurons in the respective layers of the network.
		For example, if the list was [2, 3, 1] then it would be a three-layer network, with the
		first layer containing 2 neurons, the second layer 3 neurons, and the third layer 1 neuron.
		The biases and weights for the network are initialized randomly, using a Gaussian distribution 
		with mean 0, and variance 1. Note that the first layer is assumed to be an input layer, and by 
		convention we won't set any biases for those neurons, since biases are only ever used in computing
		the outputs from later layers.
		"""
		self.num_layers = len(sizes)
		self.sizes = sizes
		self.biases = [np.random.randn(y, 1) for y in sizes[1:]]
		self.weights = [np.random.randn(y, x) for x, y in zip(sizes[:-1], sizes[1:])]
		print(self.biases[0].shape, self.weights[0].shape)
		print(self.biases[1].shape, self.weights[1].shape)

	def feedforward(self, a):
		"""
		Return the output of the network if 'a' is input.
		"""
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
			mini_batches = [ training_data[ k : k + mini_batch_size ] for k in range(0, n, mini_batch_size) ]
			for mini_batch in mini_batches:
				self._update_mini_batch(mini_batch, lr)
			if test_data:
				print("Epoch {}; train accuracy : {} ; test accuracy : {}".format(j, train_accuracy, self._evaluate(test_data)/n_test));
			else:
				print("Epoch {} complete".format(j))

	def predict(test):
		# with open('results.txt', 'w') as f:
		for i in range(len(test)):
			print(np.argmax(self.feedforward(test[i])))

	def _update_mini_batch(self, mini_batch, lr):
		"""
		Update the network's weights and biases by applying
		gradient descent using backpropagation to a single mini batch.
		The 'mini_batch' is a list of tuples '(x, y)', and 'lr' is the learning rate.
		"""
		nabla_b = [np.zeros(b.shape) for b in self.biases]
		nabla_w = [np.zeros(w.shape) for w in self.weights]
		for x, y in mini_batch:
			delta_nabla_b, delta_nabla_w = self._backprop(x, y)
			nabla_b = [nb+dnb for nb, dnb in zip(nabla_b, delta_nabla_b)]
			nabla_w = [nw+dnw for nw, dnw in zip(nabla_w, delta_nabla_w)]
		self.weights = [ w - (lr / len(mini_batch) ) * nw for w, nw in zip(self.weights, nabla_w)]
		self.biases = [b-(lr/len(mini_batch))*nb  for b, nb in zip(self.biases, nabla_b)]

	def _backprop(self, x, y):
		"""
		Return a tuple '(nabla_b, nabla_w)' representing the
		gradient for the cost function C_x.  'nabla_b' and
		'nabla_w' are layer-by-layer lists of numpy arrays, similar
		to 'self.biases' and 'self.weights'.
		"""
		nabla_b = [np.zeros(b.shape) for b in self.biases]
		nabla_w = [np.zeros(w.shape) for w in self.weights]
		# feedforward
		activation = x
		activations = [x] # list to store all the activations, layer by layer
		zs = [] # list to store all the z vectors, layer by layer
		for b, w in zip(self.biases, self.weights):
			z = np.dot(w, activation)+b
			print(z.shape)
			zs.append(z)
			activation = sigmoid(z)
			activations.append(activation)
		# backward pass
		delta = self._cost_derivative(activations[-1], y) * sigmoid_prime(zs[-1])
		nabla_b[-1] = delta
		nabla_w[-1] = np.dot(delta, activations[-2].transpose())
		# Note that the variable l in the loop below is used a little
		# differently to the notation in Chapter 2 of the book.  Here,
		# l = 1 means the last layer of neurons, l = 2 is the
		# second-last layer, and so on.  It's a renumbering of the
		# scheme in the book, used here to take advantage of the fact
		# that Python can use negative indices in lists.
		for l in range(2, self.num_layers):
			z = zs[-l]
			sp = sigmoid_prime(z)
			delta = np.dot(self.weights[-l+1].transpose(), delta) * sp
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
	return 1.0 / ( 1.0 + np.exp(-x) )

def sigmoid_prime(x):
	return sigmoid(x) * ( 1 - sigmoid(x) )



if __name__ == '__main__':
	# gen_img_to_see('train_img')
	# gen_img_to_see('test_img')
	layers = [784, 2, 3]
	lr = 0.01
	ep = 1000
	batch_size = 3

	train_data, test_data, test = readData()

	model = Network(layers)
	model.train(train_data, ep, batch_size, lr, test_data)
	# model.predict(test)














