import numpy as np
import matplotlib.pyplot as plt

# This whole function was created in conjunction with the times.txt file, which were different times 
# needed for a certain calculation (an integral, if I recall).
# This data is displayed in a neat histogram
# What I learned: Matplotlib is freaking awesome.

g = open('times.txt', 'r')
s = '\n'
v = []
count = 0
while True:
	s = g.readline()
	if '\n' not in s:
		break
	v.append(float(s.split()[1]))
	count += 1
g.close()

plt.hist(v, bins=50)       # matplotlib version (plot)
plt.show()