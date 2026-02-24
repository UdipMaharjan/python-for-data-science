import numpy as np
arr=np.array([1,2,3,4,5,6,7])
print(arr[2])

a=np.array([[1,2,3,4,5],[4,5,6,7,8]])
print(a[1,2])

#Slicing

b = np.array([1, 2, 3, 4, 5, 6, 7])
print(b[1:5])

c = np.array([1, 2, 3, 4, 5, 6, 7])
print(c[1:5:2])

#Datatypes

d = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]], dtype='S')
print(d[0:2, 1:4])

e = np.array(["Hello","World",'Goal'])
print(e.dtype)
print(d.dtype)

arr = np.array([1.1, 2.1, 3.1], dtype='i')
print(arr)
print(arr.dtype)

# Changing data type
ds = np.array([1.1, 2.1, 3.1])
newarr = ds.astype('i')
print(newarr)
print(newarr.dtype)

#Copy

ab=np.array([1,2,3,4,5,6])
sb=ab.copy()
ab[1]=12
print(sb)
print(ab)
print(sb.base)

#View

rn=np.array([1,2,3,4,5,6])
pr=rn.view()
pr[1]=12
print(pr)
print(rn)
print(pr.base)
