import math

def integral(f, x0, xf):
	''' Simpson's rule, integral of f from x0 to xf.
		Uses 10000 steps as it currently stands
	'''


	x0 = float(x0) # To avoid type/rounding error
	n = 10000

	n = n - (n % 2) # Forces n to be even, in case it isn't

	step = (xf-x0)/n
	ans = f(x0) + f(xf)
	for i in range(1, n, 2):
		ans += 4 * f(i * step + x0)
	for i in range(2, n-1, 2):
		ans += 2 * f(i * step + x0)

	return ans * step / 3


def f(x):
	return math.e ** - (x ** 2)

print integral(f, 0, 10000)