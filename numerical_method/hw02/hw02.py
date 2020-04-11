import numpy as np
import time



N = [2, 3, 4, 10, 100, 500, 1000, 5000, 10000]



print('|   n  |            time')
print('|------|--------------------------------|')
for n in N:
	a = np.random.rand(n, n)
	b = np.random.rand(n, 1)

	t = time.time()
	x = np.linalg.solve(a, b)
	t = time.time() - t
	# print(f'|{n:>6}| {t:.25f} sec|')

	if n < 5:
		print(f'### n = {n}\n')
		print('#### func:\n')
		for i in range(n):
			print('$', end='')
			for j in range(n):
				if a[i][j] >= 0 and j != 0 :
					print('+', end='')
				print(f'{a[i][j]:.6f}X_{{{j}}}', end="")
			print(f' = {b[i][0]:.6f}$')
		print('#### ans:\n')
		for i in range(n):
			print(f'$X_{{{i}}} = {x[i][0]:.6f}$ $,$ ', end='')
	print()
