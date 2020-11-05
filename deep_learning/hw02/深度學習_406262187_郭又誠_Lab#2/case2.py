import matplotlib.pyplot as plt
from gradient_descent import GDA

if __name__ == '__main__':
	data = [[0, 0, 0],
			[0, 1, 1],
			[1, 0, 1],
			[1, 1, 1]]

	gda = GDA(2)
	gda.train(data)

	train_1 = []
	train_0 = []

	for i in range(len(data)):
		if data[i][2] == 1:
			train_1.append((data[i][0], data[i][1]))
		else:
			train_0.append((data[i][0], data[i][1]))

	plt.plot([0., 1.], [-(gda.w[1] * 0 + gda.w[0]) / gda.w[2], -(gda.w[1] * 1 + gda.w[0]) / gda.w[2]], 'b', label='Train')
	plt.plot([0., 1.], [-(gda.w_init[1] * 0. + gda.w_init[0]) / gda.w_init[2], -(gda.w_init[1] * 1. + gda.w_init[0]) / gda.w_init[2]], '--r', label='Init')
	plt.plot([i[0] for i in train_1], [i[1] for i in train_1], '.k', label='1 (Training)')
	plt.plot([i[0] for i in train_0], [i[1] for i in train_0], 'xr', label='0 (Training)')
	plt.legend(loc='lower left', shadow=True)
	plt.show()