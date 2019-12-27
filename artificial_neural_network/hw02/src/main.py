import math
import random
import time
from neuron import *

TraningFile = open("iris_training_data.txt","r")
TestFile = open("iris_testing_data.txt","r")
OutputFile = open("Output.out","w")
TrainData = []
TestData = []

def readFile() :

	global TrainData
	global TestData
	TrainData = []
	TestData = []

	for i in TraningFile.readlines() :
		A,B,C,D,Kind = i.split()
		data = ((float(A),float(B),float(C),float(D)),UCI(Kind))
		TrainData.append(data)

	for i in TestFile.readlines() :
		A,B,C,D,Kind = i.split()
		data = ((float(A),float(B),float(C),float(D)),UCI(Kind))
		TestData.append(data)

def UCI(Kind) :
	if Kind == "versicolor":
		return [0.9, 0.1, 0.1]
	if Kind == "virginica":
		return [0.1, 0.9, 0.1]
	if Kind == "setosa":
		return [0.1, 0.1, 0.9]

def main(HiddenNum,LRate) :
	
	Network = NeuralNetwork(LRate)
	HiddenLayer = NeuronLayer(4,HiddenNum)
	OutputLayer = NeuronLayer(HiddenNum,3)

	Network.addLayer(HiddenLayer)
	Network.addLayer(OutputLayer)

	Epoch = 1
	EpochLimit = 1000000
	while Epoch < EpochLimit and Network.countError(TrainData) > 0.01 :
		Network.train(TrainData)
		print("Train {}, {}".format(Epoch,Network.countError(TrainData)))
		Epoch += 1
	# Training Data

	print("Number of hidden neurons = {}".format(HiddenNum), file=OutputFile)
	print("Learning rates = {}".format(LRate), file= OutputFile)

	# print("**********************", file=OutputFile)
	AC = 0
	for inputs,outputs in TrainData :
		# print("{}, {}".format(Network.getOutput(inputs),outputs), file=OutputFile)
		if Network.getOutput(inputs) == outputs :
			AC += 1
	# print("**********************", file=OutputFile)
	print("training accuracies = {}%".format(AC/len(TrainData)*100), file=OutputFile)
	
	# print("**********************", file=OutputFile)
	AC = 0
	for inputs,outputs in TestData :
		# print("{}, {}".format(Network.getOutput(inputs),outputs), file=OutputFile)
		if Network.getOutput(inputs) == outputs :
			AC += 1
	# print("**********************", file=OutputFile)
	print("test accuracies = {}%".format(AC/len(TestData)*100), file=OutputFile)
	print("epochs = {}".format(Epoch), file=OutputFile)
	print("-----------------------------------", file = OutputFile)


LRate = [1.0, 0.5, 0.1]
HiddenNum = [1, 5, 10, 15, 30, 50]

if __name__ == "__main__" :
	readFile()
	for i in HiddenNum :
		for j in LRate :
			main(i,j)
			print("Completed {},{}".format(i,j))