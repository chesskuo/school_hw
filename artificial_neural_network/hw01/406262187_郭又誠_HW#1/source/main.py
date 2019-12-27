import numpy as np
import random
import time

# ======================================== #
#              user config                 #
# ======================================== #

dataset = 2 # select dataset
neuron = 4 # select number fo neuron
components = 2
times = 1 # test times
lr = 1.0 # learning rate

# ======================================== #





if dataset == 2:
	filename = f'd{dataset:d}_{neuron:d}neuron_{components:d}comp.out'
else:
	filename = f'd{dataset:d}_{neuron:d}neuron.out'

output = open(filename, "w") # output file





def Init():
	global weight
	global biases
	global W
	global B
	global P
	global O
	if neuron == 2:
		W = np.array([[0.0],[0.0]])
		B = np.array([[0.0],[1.0]])
		P = np.array([[1.0],[0.0]])
		O = np.array([[1.0],[1.0]])
		if dataset == 1:
			weight = np.array([
					[1.0, 0.0],
					[0.0, 1.0]
				])
			biases = np.array([
				[1.0],
				[1.0]
			])
		elif dataset == 2:
			if components == 2:
				weight = np.array([
					[1.0, 0.0],
					[0.0, 1.0]
				])
				biases = np.array([
					[1.0],
					[1.0]
				])
			else:
				weight = np.array([
						[0.0, 0.0, 0.0],
						[0.0, 0.0, 0.0]
					])
				biases = np.array([
						[0.0],
						[0.0]
					])
				for i in range(2):
					for j in range(3):
						weight[i][j] = random.uniform(-10.0, 10.0)
				for i in range(2):
					biases[i] = random.uniform(-10.0, 10.0)
	elif neuron == 4:
		W = np.array([[1.0],[0.0],[0.0],[0.0]])
		B = np.array([[0.0],[1.0],[0.0],[0.0]])
		P = np.array([[0.0],[0.0],[1.0],[0.0]])
		O = np.array([[0.0],[0.0],[0.0],[1.0]])
		if dataset == 1 or components == 2:
			weight = np.array([
					[0.0, 0.0],
					[0.0, 0.0],
					[0.0, 0.0],
					[0.0, 0.0]
				])
			biases = np.array([
					[0.0],
					[0.0],
					[0.0],
					[0.0]
				])
			for i in range(4):
				for j in range(2):
					weight[i][j] = random.uniform(-10.0, 10.0)
			for i in range(2):
				biases[i] = random.uniform(-10.0, 10.0)
		elif dataset == 2:
			weight = np.array([
					[0.0, 0.0, 0.0],
					[0.0, 0.0, 0.0],
					[0.0, 0.0, 0.0],
					[0.0, 0.0, 0.0]
				])
			biases = np.array([
					[0.0],
					[0.0],
					[0.0],
					[0.0]
				])
			for i in range(4):
				for j in range(3):
					weight[i][j] = random.uniform(-10.0, 10.0)
			for i in range(4):
				biases[i] = random.uniform(-10.0, 10.0)





def Training():
	global dataset

	trainingData = open('dataset' + str(dataset) + '/training_data.txt', 'r')
	data = list()

	for i in trainingData.readlines():
		if dataset == 1:
			a, b, t = i.split()
			tmpIn = np.array([[float(a)], [float(b)]])
		elif dataset == 2:
			a, b, c, t = i.split()
			if components == 2:
				tmpIn = np.array([[float(a)], [float(b)]])
			else:
				tmpIn = np.array([[float(a)], [float(b)], [float(c)]])
		tmpOut = TypeToMat(t)
		data.append(np.array([tmpIn, tmpOut]))
	trainingData.close()

	global weight
	global biases
	global epoch

	ok = False
	epoch = 1

	while True:
		if ok:
			break
		ok = True
		for i in data:
			tmp = HardLim(weight.dot(i[0]) + biases)
			e = i[1] - tmp
			if Check(e):
				weight = weight + lr * e.dot(i[0].T)
				biases = biases + lr * e
				ok = False

		epoch += 1

def Check(e):
	for i in e:
		if i != 0.0:
			return True
	return False

def HardLim(m):
	ret = np.array([[0.0]])
	for i in m:
		if i >= 0.0:
			ret = np.append(ret, [[float(1.0)]], axis=0)
		else:
			ret = np.append(ret, [[float(0.0)]], axis=0)
	ret = np.delete(ret, 0, axis=0)
	return ret

def TypeToMat(t):
	if t == "W" :
		return W
	if t == "B" :
		return B
	if t == "P" :
		return P
	if t == "O" :
		return O





def Testing():
	testingData = open('dataset' + str(dataset) + '/testing_data.txt', 'r')
	data = list()

	for i in testingData.readlines():
		if dataset == 1:
			a, b = i.split()
			data.append(np.array([[float(a)], [float(b)]]))
		elif dataset == 2:
			a, b, c = i.split()
			if components == 2:
				data.append(np.array([[float(a)], [float(b)]]))
			else:
				data.append(np.array([[float(a)], [float(b)], [float(c)]]))
	testingData.close()

	global en

	en = 0

	for i in data:
		out = HardLim(weight.dot(i) + biases)
		out = Decide(out)
		if out == 'Error':
			en += 1
		print(out, file=output)

def Decide(m) :
	if np.array_equal(m,W):
		return "W"
	if np.array_equal(m,B):
		return "B"
	if np.array_equal(m,P):
		return "P"
	if np.array_equal(m,O):
		return "O"
	return "Error"



if __name__ == "__main__":
	totalError = 0
	totalTime = 0.0

	for i in range(times):
		print(f'Test Times: {i+1:d}', end='\n\n', file=output)

		Init()
		print('Initial', end='\n\n', file=output)
		print('Weight:', file=output)
		print(weight, end='\n\n', file=output)
		print('Biases:', file=output)
		print(biases, end='\n\n', file=output)
		print('----------', file=output)

		thisTime = time.time()
		Training()
		thisTime = time.time() - thisTime
		totalTime += thisTime
		print('After Training', end='\n\n', file=output)
		print('Weight:', file=output)
		print(weight, end='\n\n', file=output)
		print('Biases:', file=output)
		print(biases, end='\n\n', file=output)
		print('----------', file=output)

		print("Result:", file=output)
		Testing()

		print(f'Total Epoch: {epoch:d}', file=output)
		print(f'Error Times: {en:d}', file=output)
		print(f'Using time: {thisTime:.4f} seconds', file=output)

		totalError += en

		print(file=output)
		print('==============================', file=output)
		
	print(f'Total Error: {totalError:d}', file=output)
	print(f'Total time using: {totalTime:.4f} seconds', file=output)