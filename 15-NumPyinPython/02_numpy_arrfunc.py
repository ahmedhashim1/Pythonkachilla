import numpy as np

a = np.array([10,12,15,2,4,6,100,320,0.5,10.3])
# a.sort()
print(a)
b = np.array([10.2,3.4,53.6,91.6,45.5])
print(b)

#concate
c = np.concatenate((a, b))
c.sort()
print(c)