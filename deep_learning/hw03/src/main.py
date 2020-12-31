from PIL import Image
import numpy as np
import os
from backpropagation import *




epochLimit = 100000






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

def training() :
	
	network = NeuralNetwork(0.1)
	hiddenLayer = NeuronLayer(784, 1)
	outputLayer = NeuronLayer(1, 3)

	network.add_layer(hiddenLayer)
	network.add_layer(outputLayer)

	epoch = 1
	curErr = 1

	while (epoch < epochLimit) and (curErr > 0.2):
		network.train(trainData)
		curErr = network.calculate_total_error(trainData)
		if epoch % 5000 == 0 or True:
			print(f'-[RUN] Training ... {epoch :d}, {curErr :f}')
		epoch += 1



def read_data():

	global trainData
	global testData

	trainData = []
	testData = []

	with open('../train_img.txt', 'r') as f:
		tmp_d = f.readlines()
	with open('../train_label.txt', 'r') as f:
		tmp_t = f.readlines()

	for i in range(len(tmp_t)//8000):
		tmp = tmp_d[i].strip().split(',')
		train_d = []
		train_t = []
		for j in tmp:
			train_d.append(float(j))
		# print(len(train_d))
		trainData.append((train_d, trans_UCI(tmp_t[i].strip())))

def trans_UCI(kind) :
	if kind == '0':
		return [1., 0., 0.]
	elif kind == '1':
		return [0., 1., 0.]
	elif kind == '2':
		return [0., 0., 1.]










if __name__ == '__main__':
	# gen_img_to_see('train_img')
	# gen_img_to_see('test_img')
	read_data()
	training()