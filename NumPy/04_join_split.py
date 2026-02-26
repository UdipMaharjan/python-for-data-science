import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.concatenate((arr1, arr2))
print(arr)

arr3 = np.array([[1, 2], [3, 4]])
arr4 = np.array([[5, 6], [7, 8]])
arr5 = np.concatenate((arr3, arr4), axis=1)
print(arr5)

arr6 = np.array([1, 2, 3])
arr7 = np.array([4, 5, 6])
arr8 = np.stack((arr6, arr7), axis=1)
print(arr8)

arr9 = np.array([1, 2, 3])
arr10 = np.array([4, 5, 6])
arr11 = np.hstack((arr9, arr10))
print(arr11)

arr12 = np.array([1, 2, 3])
arr13 = np.array([4, 5, 6])
arr14 = np.vstack((arr12, arr13))
print(arr14)

#Split

arr15 = np.array([1, 2, 3, 4, 5, 6])
arr16 = np.array_split(arr15, 3)
print(arr16)


arr17 = np.array([1, 2, 3, 4, 5, 6])
arr18 = np.array_split(arr17, 4)
print(arr18)

arr19 = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
arr20 = np.array_split(arr19, 3)
print(arr20)