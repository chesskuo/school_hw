import math
import random

# 所有的神經元
class Neuron(object):

	def __init__(self,weightNum):
		self.inputs = []
		self.weights = []
		self.bias = random.uniform(0.0, 1.0)
		self.output = 0.0
		self.delta = 0.0
		for i in range(weightNum):
			self.weights.append(random.uniform(0.0, 1.0))

	def sigmoid(self,x) :
		return 1/(1+math.exp(-x))

	def calOutput(self,inputs):
		self.output = 0.0
		self.inputs = inputs
		for i in range(len(self.weights)):
			self.output += self.weights[i] * inputs[i]
		self.output = self.sigmoid(self.output+self.bias)
		return self.output
	# 計算該神經元的output並使用sigmoid函數

	def calDeltas(self, error):
		self.delta = error*self.output*(1-self.output)
	# 計算誤差值

	def update(self,learningRate):
		for i in range(len(self.weights)):
			self.weights[i] =  self.weights[i] - learningRate*self.inputs[i]*self.delta
		self.bias = self.bias - learningRate*self.delta
	# Weight 跟 Bias 的更新

# Hidden layer 跟 Output Layer
class NeuronLayer(object):

	def __init__(self,inputNum,neuronNum):
		self.neurons = []
		for i in range(neuronNum):
			n = Neuron(inputNum)
			self.neurons.append(n)

	def feedForward(self,inputs):
		outputs = []
		for n in self.neurons:
			outputs.append(n.calOutput(inputs))
		return outputs
	# 計算該層的所有output

	def getDelta(self):
		return [n.delta for n in self.neurons]
	# 拿該層所有神經元的誤差值

	def update(self,learningRate):
		for n in self.neurons:
			n.update(learningRate)
	# 對該層所有神經元更新

# 整個神經網路主體
class NeuralNetwork(object):

	def __init__(self,learningRate = 1):
		self.neuronLayers = []
		self.learningRate = learningRate

	def addLayer(self,neruonLayer):
		self.neuronLayers.append(neruonLayer)

	def feedForward(self,inputs):
		for i in self.neuronLayers :
			inputs = i.feedForward(inputs)
		return inputs
	# 計算整個神經網路

	def feedBack(self,outputs):
		lenNum = len(self.neuronLayers)
		preDeltas = []
		while lenNum :
			currentLayer = self.neuronLayers[lenNum-1]
			if len(preDeltas) == 0 : # Output Layer
				for i in range(len(currentLayer.neurons)) :
					error = -(outputs[i]-currentLayer.neurons[i].output)
					currentLayer.neurons[i].calDeltas(error)
			else : # Hidden Layer
				preLayer = self.neuronLayers[lenNum]
				for i in range(len(currentLayer.neurons)) :
					error = 0
					for j in range(len(preDeltas)) :
						error += preDeltas[j]*preLayer.neurons[j].weights[i]
					currentLayer.neurons[i].calDeltas(error)
			preDeltas = currentLayer.getDelta()
			lenNum -= 1
	# 逆推回去求各個神經元的誤差

	def update(self,learningRate) :
		for L in self.neuronLayers :
			L.update(learningRate)
	# 更新整個神經網路
	
	def train(self,data) :
		for inputs,outputs in data :
			self.feedForward(inputs)
			self.feedBack(outputs)
			self.update(self.learningRate)
	# 訓練資料

	def countError(self,data) :
		totalError = 0
		for inputs, outputs in data :
			actualOutput = self.feedForward(inputs)
			for i in range(len(outputs)) :
				totalError += (outputs[i] - actualOutput[i])**2
		return math.sqrt(totalError)/len(data)
	# 得到error的數值

	def changeOutput(self,x):
		if x[0] > x[1] and x[0] > x[2] :
			return [0.9, 0.1, 0.1]
		if x[1] > x[0] and x[1] > x[2] :
			return [0.1, 0.9, 0.1]
		if x[2] > x[0] and x[2] > x[1] :
			return [0.1, 0.1, 0.9]

	def getOutput(self, inputs) :
		OUT = self.feedForward(inputs)
		OUT = self.changeOutput(OUT)
		return OUT