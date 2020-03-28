import math
import sympy





###############################################
################# User Config #################

choose_a_function_which_you_want = 3 # only 1 ~ 4, if you are naughty... em....

tol = 10 ** -10

limit_times = 1000

###############################################










# math function
def func_1(x):
	if type(x) == type(1) or type(x) == type(1.0):
		return math.exp(x) - 3 * x * math.cos(2 * x) - 8.3
	else:
		return sympy.exp(x) - 3 * x * sympy.cos(2 * x) - 8.3

def func_2(x):
	if type(x) == type(1) or type(x) == type(1.0):
		return math.exp(x * math.sin(x)) - x * math.cos(2 * x) - 2.8
	else:
		return sympy.exp(x * sympy.sin(x)) - x * sympy.cos(2 * x) - 2.8

def func_3(x):
	if type(x) == type(1) or type(x) == type(1.0):
		try:
			ans = math.exp(x * math.exp(x))
		except OverflowError:
			ans = float('inf')
		return ans
	else:
		return sympy.exp(x * sympy.exp(x))

def func_4(x):
	if type(x) == type(1) or type(x) == type(1.0):
		return math.cos(x) * math.sin(x) * math.tan(x) - math.exp(x)
	else:
		return sympy.cos(x) * sympy.sin(x) * sympy.tan(x) - sympy.exp(x)





# algorithm function

# bisection method
def bisect(a, b, f):
	print('Bisection Method:')
	print('----------')
	root_cnt = 0
	for i in range(a, b):
		if f(i) * f(i+1) >= 0:
			continue
		else:
			x, cnt = _bisect(i, i+1, f)
			print(f"x = {x:.10f}, times = {cnt:d}")
			root_cnt += 1
	print(f'\nroots: {root_cnt:d}\n\n')
	return root_cnt

def _bisect(a, b, f):
	global tol
	global limit_times
	cnt = 0
	while abs(a - b) > tol:
		cnt += 1
		m = (a + b) / 2
		if f(a) * f(m) < 0:
			b = m
		else:
			a = m
		if cnt >= limit_times:
			return c, cnt
	return m, cnt



# false position method
def falsi(a, b, f):
	print('False Position Method:')
	print('----------')
	root_cnt = 0
	for i in range(a, b):
		if f(i) * f(i+1) >= 0:
			continue
		else:
			x, cnt = _falsi(i, i+1, f)
			print(f"x = {x:.10f}, times = {cnt:d}")
			root_cnt += 1
	print(f'\nroots: {root_cnt:d}\n\n')
	return root_cnt

def _falsi(a, b, f):
	global tol
	global limit_times
	cnt = 0
	c = b
	while abs(c - a) > tol:
		cnt += 1
		c = (a * f(b) - b * f(a)) / (f(b) - f(a))
		if f(c) == 0:
			return c, cnt
		elif f(a) * f(c) < 0:
			b = c
		else:
			a = c
		if cnt >= limit_times:
			return c, cnt
	return c, cnt



# modify false position
def modfalsi(a, b, f):
	print('Modify False Position Method:')
	print('----------')
	root_cnt = 0
	for i in range(a, b):
		if f(i) * f(i+1) >= 0:
			continue
		else:
			x, cnt = _modfalsi(i, i+1, f)
			print(f"x = {x:.10f}, times = {cnt:d}")
			root_cnt += 1
	print(f'\nroots: {root_cnt:d}\n\n')
	return root_cnt

def _modfalsi(a, b, f):
	global tol
	global limit_times
	cnt = 0
	c = b
	fa = f(a)
	fb = f(b)
	while abs(c - a) > tol:
		cnt += 1
		c = (a * f(b) - b * f(a)) / (f(b) - f(a))
		fc = f(c)
		if fc == 0:
			return c, cnt
		elif fa * fc < 0:
			b = c
			fa /= 2
			fb = f(b)
		else:
			a = c
			fa = f(a)
			fb /= 2
		if cnt >= limit_times:
			return c, cnt
	return c, cnt



# Secant Method（割線法）
def sect(a, b, f):
	print('Secant Method:')
	print('----------')
	root_cnt = 0
	for i in range(a, b):
		if f(i) * f(i+1) >= 0:
			continue
		else:
			x, cnt = _modfalsi(i, i+1, f)
			print(f"x = {x:.10f}, times = {cnt:d}")
			root_cnt += 1
	print(f'\nroots: {root_cnt:d}\n\n')
	return root_cnt

def _sect(a, b, f):
	global tol
	global limit_times
	cnt = 0
	while abs(c - a) > tol:
		cnt += 1
		c = (a * f(b) - b * f(a)) / (f(b) - f(a))
		a = b
		b = c
		if cnt >= limit_times:
			return b, cnt
	return b, cnt



# Newten's Method
def newten(a, b, f):
	print("Newten's Method:")
	print('----------')
	root_cnt = 0
	for i in range(a, b):
		if f(i) * f(i+1) >= 0:
			continue
		else:
			x, cnt = _newten(i, f)
			print(f"x = {x:.10f}, times = {cnt:d}")
			root_cnt += 1
	print(f'\nroots: {root_cnt:d}\n\n')
	return root_cnt

def _newten(a, f):
	global tol
	global limit_times
	cnt = 0
	x = sympy.symbols('x', communtative = True)
	df = sympy.symbols('df', cls = sympy.Function)
	df = sympy.diff(f(x), x)
	d = -f(a) / float(df.evalf(subs = {x:a}))
	while abs(d) > tol:
		cnt += 1
		a += d
		d = -f(a) / float(df.evalf(subs = {x:a}))
		if cnt >= limit_times:
			return a, cnt
	return a, cnt



# Fixied Point Method（固定點法）
def fixied(a, b, f):
	print('Fixied Method:')
	print('----------')
	root_cnt = 0
	for i in range(a, b):
		if f(i) * f(i+1) >= 0:
			continue
		else:
			x, cnt = _fixied(i, f)
			print(f"x = {x:.10f}, times = {cnt:d}")
			root_cnt += 1
	print(f'\nroots: {root_cnt:d}\n\n')

def _fixied(a, f):
	global tol
	global limit_times
	cnt = 0
	tmp = a + 2 * tol
	while abs(tmp - a) > tol:
		cnt += 1
		tmp = a
		a = f(a)
		if cnt >= limit_times:
			return a, cnt
	return a, cnt





if __name__ == '__main__':

	if choose_a_function_which_you_want == 1:
		a = -10
		b = 2
		bisect(a, b, func_1)
		falsi(a, b, func_1)
		modfalsi(a, b, func_1)
		sect(a, b, func_1)
		newten(a, b, func_1)
		fixied(a, b, func_1)
	elif choose_a_function_which_you_want == 2:
		a = -5
		b = 5
		bisect(a, b, func_2)
		falsi(a, b, func_2)
		modfalsi(a, b, func_2)
		sect(a, b, func_2)
		newten(a, b, func_2)
		fixied(a, b, func_2)
	elif choose_a_function_which_you_want == 3:
		a = 0
		b = 10
		bisect(a, b, func_3)
		falsi(a, b, func_3)
		modfalsi(a, b, func_3)
		sect(a, b, func_3)
		newten(a, b, func_3)
		fixied(a, b, func_3)
	elif choose_a_function_which_you_want == 4:
		a = -10
		b = 0
		bisect(a, b, func_4)
		falsi(a, b, func_4)
		modfalsi(a, b, func_4)
		sect(a, b, func_4)
		newten(a, b, func_4)
		fixied(a, b, func_4)
	else:
		print("Don't 調皮 ~")
		print("就跟你說 1 到 4 了")