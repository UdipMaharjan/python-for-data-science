import numpy as np
arr=np.array([1,2,3])
print(arr)
print(type(arr))
arr[0]=100
print(arr)
print(np.__version__)

#2D Array

a=np.array([[1,2,3],[4,5,6]])
print(type(a))
print(a.ndim) #Check dimension
print(a[0,1])

#3D Array 
b=np.array([[[1,2,3],[4,5,6]]])
print(b.ndim)
print(b[0,1,2])

c = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(c[0,0,2])

