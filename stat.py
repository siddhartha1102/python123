import numpy
from matplotlib import pyplot as plt
import matplotlib

num=[39,116,24,122,83,59,77,97,88,86,95,110,61]

x=sorted(num)
print("array elements")

for l in x:
	print(l)
	pass


print("Standard deviation ",numpy.std(x))
print("Variance",numpy.var(x))

plt.hist(x,max(num))
plt.show()
