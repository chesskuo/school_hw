import matplotlib.pyplot as plt
from gradient_descent import GDA

if __name__ == '__main__':
	data = [[170, 80, 1],
			[90, 15, 0],
			[130, 30, 0],
			[165, 55, 1],
			[150, 45, 1],
			[120, 40, 0],
			[110, 35, 0],
			[180, 70, 1],
			[175, 65, 1],
			[160, 60, 1]]

	data2 = [[170, 60],
			[85, 15],
			[145, 45]]

	gda = GDA(2)
	gda.train(data)

	train_1 = []
	train_0 = []

	for i in range(len(data)):
		if data[i][2] == 1:
			train_1.append((data[i][0], data[i][1]))
		else:
			train_0.append((data[i][0], data[i][1]))

	test_t = gda.test(data2)
	test_1 = []
	test_0 = []

	for i in range(len(data2)):
		if test_t[i] == 1:
			test_1.append((data2[i][0], data2[i][1]))
		else:
			test_0.append((data2[i][0], data2[i][1]))

	plt.plot([0., 200.], [-(gda.w[1] * 0. + gda.w[0]) / gda.w[2], -(gda.w[1] * 200. + gda.w[0]) / gda.w[2]], 'b', label='Train')
	plt.plot([0., 100.], [-(gda.w_init[1] * 0. + gda.w_init[0]) / gda.w_init[2], -(gda.w_init[1] * 100. + gda.w_init[0]) / gda.w_init[2]], '--r', label='Init')
	plt.plot([i[0] for i in train_1], [i[1] for i in train_1], '.k', label='1 (Training)')
	plt.plot([i[0] for i in train_0], [i[1] for i in train_0], 'xr', label='0 (Training)')
	plt.plot([i[0] for i in test_1], [i[1] for i in test_1], '^k', label='1 (Testing)')
	plt.plot([i[0] for i in test_0], [i[1] for i in test_0], '^r', label='0 (Testing)')
	plt.legend(loc='lower left', shadow=True)
	plt.show()