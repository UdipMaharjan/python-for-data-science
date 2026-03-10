import numpy
from numpy import random
x=random.randint(100)
print(x)

y=random.rand()
print(y)

z=random.randint(100, size=(5))
print(z) #1-D array contaning 5 random integers from 0 to 100

v=random.rand(5)
print(v)

r=random.rand(3, 5)
print(r)

p=random.choice([1,2,3,4,5])
print(p)

pr = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(100))
print(pr)

#Data distribution

xr = random.choice([5, 2, 7], p=[0.1, 0.3, 0.6], size=(100))
print(xr)

xp = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(3, 5))
print(xp)

#Permutation and Shuffle

#Doesn't change the original array
zz=numpy.array([1,2,3,4,5])
print(random.permutation(zz))

#Changes the original array
rr=numpy.array([1,2,3,4,5])
ss=random.shuffle(rr)
print(rr)

