import numpy as np

#creating an 1D array using numpy
food = np.array(["Pakora", "Samosa", "Raita"])
price = np.array([5,5,5])
# print(type(food))
print(food[1])
print(price.mean())

#zeros method
z = np.zeros(6)
print(z)

#ones method
o = np.ones(6)
print(o)

#empty
e = np.empty(5)
print(e)

#using range
r = np.arange(10)
print(r)

#specify range
sr = np.arange(2,20)
print(sr)

#specify range with interval
sri = np.arange(2,20,2)
print(sri)

#table of 5
tbf = np.arange(5,55,5)
print(tbf)

#line space
ls = np.linspace(1,100,num=10)
print(ls)

#specify data type
dt = np.ones(5,dtype=np.float64)
print(dt)