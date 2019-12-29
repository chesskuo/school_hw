import math
import random
import time
from backpropagation import *

# ======================================== #
#              user config                 #
# ======================================== #

trainIn = open("iris_training_data.txt", "r")
testIn = open("iris_testing_data.txt", "r")
fileOut = open("result.txt", "w")

lr_list = [1.0, 0.5, 0.1]
hidden_num_list = [1, 10, 20, 30]

epochLimit = 1000

# ======================================== #





def read_data():

	global trainData
	global testData

	trainData = []
	testData = []

	for i in trainIn.readlines() :
		a, b, c, d, kind = i.split()
		data = ((float(a), float(b), float(c), float(c)), trans_UCI(kind))
		trainData.append(data)

	for i in testIn.readlines() :
		a, b, c, d, kind = i.split()
		data = ((float(a), float(b), float(c), float(d)), trans_UCI(kind))
		testData.append(data)

def trans_UCI(kind) :
	if kind == 'versicolor':
		return [0.9, 0.1, 0.1]
	elif kind == 'virginica':
		return [0.1, 0.9, 0.1]
	elif kind == 'setosa':
		return [0.1, 0.1, 0.9]



def training(hidden_num, lr) :
	
	network = NeuralNetwork(lr)
	hiddenLayer = NeuronLayer(4, hidden_num)
	outputLayer = NeuronLayer(hidden_num, 3)

	network.add_layer(hiddenLayer)
	network.add_layer(outputLayer)

	epoch = 1
	curErr = 1

	while (epoch < epochLimit) and (curErr > 0.02):
		network.train(trainData)
		curErr = network.calculate_total_error(trainData)
		if epoch % 5000 == 0:
			print(f'-[RUN] Training ... {epoch :d}, {curErr :f}')
		epoch += 1

	print(f'Number of hidden neurons = {hidden_num :d}', file=fileOut)
	print(f'Learning rates = {lr :f}', file= fileOut)

	ac = 0
	for inputs,outputs in trainData :
		if network.get_output(inputs) == outputs :
			ac += 1
	print(f'training accuracies = {ac / len(trainData) * 100 :f}%', file=fileOut)
	
	ac = 0
	for inputs,outputs in testData :
		if network.get_output(inputs) == outputs :
			ac += 1
	print(f'test accuracies = {ac / len(testData) * 100 :f}%', file=fileOut)

	print(f'epochs = {epoch :d}', file=fileOut)
	print('-----------------------------------', file = fileOut)

	





if __name__ == '__main__' :
	read_data()

	total = 0.0

	for i in hidden_num_list :
		for j in lr_list :
			t = time.time()
			training(i, j)
			t = time.time() - t

			total += t

			rc = open(f'hn{i:d}-lr{j:f}.txt', 'w')
			print(f'using time: {t:f} s', file=rc)
			rc.close()

			print(f'+[OK] hn={i:d}, lr={j:f}')