import numpy as np

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(arr.shape)

a = np.array([1, 2, 3, 4], ndmin=5)
print(a)
print('shape of array :', a.shape)

#reshape

z = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = z.reshape(4, 3)
print(newarr)

v = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
n = v.reshape(2, 3, 2)
print(n)

r = np.array([[1, 2, 3], [4, 5, 6]])
s = r.reshape(-1)
print(s)

print(r.flatten('C'))

#Iterate

vr=np.array([1,2,3,4,5])
for i in vr:
    print(i)

zz=np.array([[1,2,3,4,5],[6,7,8,9,10]])
for lv in zz:
    print(lv)

cc=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
for l in cc:
    for v in l:
        print(v)  

gc = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

for x in np.nditer(gc):
  print(x)

