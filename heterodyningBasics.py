import numpy as np
import matplotlib.pyplot as plt

''' Program creates a frequency v heterodyne function which 'plucks out' the 
	fundamental frequencies of the sinusoids. 
'''


def f(x, amp, omega):
	''' It's just a sine wave, fyi'''
	return amp * np.sin(x * omega)


y = []
for i in range(1000):
	y.append(np.random.normal(0,1) + f(i, 10, 0.06) + f(i, 5, 0.1))

#
# Y is now some data that has noise. It has 1000 data points. 
# Embedded are two sine waves. We are hoping to scrape them out of there.
# 


g = []
stepsize = 0.005
for a in np.arange(0, 1, stepsize):
	temp = 0
	for j in range(1000): 						# Note the 1000 
		temp += (np.sin(a*j)*y[j])		# Lazy integral equivalent
	g.append(temp)

# Cuts out a lot of the noise and prints the things that are too low to be significant
for i in range(len(g)):
	g[i] *= stepsize
	if g[i] < 1:
		g[i] = 0
	if g[i] > 10:
		print "(%.3f, %.3f) " % (i * stepsize, g[i])

plt.plot(g)
plt.show()