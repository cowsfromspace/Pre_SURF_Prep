import numpy as np
import matplotlib.pyplot as plt

''' Program plots the noisy sum of two sine waves & their clean counterpart
	Used only to show basics of numpy.
'''


def f(x, amp, omega):
	return amp * np.sin(x * omega)

y = []
g = []
for i in range(1000):
	y.append(np.random.normal(0,1))
	g.append(0)

for i in range(1000):
	val = f(i, 10, 0.06) + f(i, 5, 0.12)
	y[i] += val
	g[i] += val

plt.plot(g)
plt.plot(y)
plt.show()