import math
import random

class NeuralNetwork(object):

	def __init__(self, learning_rate=1.0):
		self.neuron_layers = []
		self.learning_rate = learning_rate

	def train(self, dataset):
		for inputs, outputs in dataset:
			self.feed_forward(inputs)
			self.feed_backword(outputs)
			self.update_weights(self.learning_rate)

	def feed_forward(self, inputs):
		for i in self.neuron_layers:
			inputs = i.feed_forward(inputs)
		return inputs

	def feed_backword(self, outputs):
		layer_num = len(self.neuron_layers)
		l = layer_num
		previous_deltas = [] 
		while l != 0:
			current_layer = self.neuron_layers[l - 1]
			if len(previous_deltas) == 0:
				for i in range(len(current_layer.neurons)):
					error = -(outputs[i] - current_layer.neurons[i].output)
					current_layer.neurons[i].calculate_delta(error)
			else:
				previous_layer = self.neuron_layers[l]
				for i in range(len(current_layer.neurons)):
					error = 0
					for j in range(len(previous_deltas)):
						error += previous_deltas[j] * previous_layer.neurons[j].weights[i]
					current_layer.neurons[i].calculate_delta(error)
			previous_deltas = current_layer.get_deltas()
			l -= 1

	def update_weights(self, learning_rate):
		for l in self.neuron_layers:
			l.update_weights(learning_rate)

	def calculate_total_error(self, dataset):
		"""
		Return mean squared error of dataset
		"""
		total_error = 0
		for inputs, outputs in dataset:
			actual_outputs = self.feed_forward(inputs)
			for i in range(len(outputs)):
				total_error += (outputs[i] - actual_outputs[i]) ** 2
		return total_error / len(dataset)

	def changeOutput(self, x):
		if (x[0] > x[1]) and (x[0] > x[2]):
			return [0.9, 0.1, 0.1]
		if (x[1] > x[0]) and (x[1] > x[2]):
			return [0.1, 0.9, 0.1]
		if (x[2] > x[0]) and (x[2] > x[1]):
			return [0.1, 0.1, 0.9]

	def get_output(self, inputs):
	   return self.changeOutput(self.feed_forward(inputs))

	def add_layer(self, neruon_layer):
		self.neuron_layers.append(neruon_layer)





class NeuronLayer(object):

	def __init__(self, input_num, neuron_num, init_weights=[], bias=1):
		self.neurons = []
		weight_index = 0
		for i in range(neuron_num):
			n = Neuron(input_num)
			self.neurons.append(n)

	def feed_forward(self, inputs):
		outputs = []
		for n in self.neurons:
			outputs.append(n.calculate_output(inputs))
		return outputs

	def get_deltas(self):
		return [n.delta for n in self.neurons]

	def update_weights(self, learning_rate):
		for n in self.neurons:
			n.update_weights(learning_rate)





class Neuron(object):

	def __init__(self, weight_num):
		self.weights = []
		self.bias = random.uniform(0.0, 1.0)
		self.output = 0
		self.delta = 0
		self.inputs = []
		for i in range(weight_num):
			self.weights.append(random.uniform(0.0, 1.0))

	def activation_function(self, x):
		"""Using sigmoid function"""
		return 1 / (1 + math.exp(-x))

	def calculate_delta(self, error):
		""" Using g' of sigmoid """
		self.delta = error * self.output * (1 - self.output)

	def update_weights(self, learning_rate):
		for (i, w) in enumerate(self.weights):
			new_w = w - learning_rate * self.delta * self.inputs[i]
			self.weights[i] = new_w
		self.bias = self.bias - learning_rate * self.delta

	def calculate_output(self, inputs):
		self.inputs = inputs
		if len(inputs) != len(self.weights):
			raise Exception("Input number not fit weight number")
		self.output = 0
		for (i, w) in enumerate(self.weights):
			self.output += w * inputs[i]
		self.output = self.activation_function(self.output + self.bias)
		return self.output