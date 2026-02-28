import numpy as np 
arr1=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr1[:,0])
x=np.where(arr1==4)
print(x)

arr2 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])

z = np.where(arr2%2 != 0)
print(z)

arr3=arr2[:10]
print("ARR3 is",arr3)
for i in arr3:
    if i%2!=0:
        print(i)
#Sort
arr4=np.array([1,11,13,14,2,6,4,9,10,22,19])
l=np.sort(arr4)
print(l)

arr5 = np.array(['banana', 'cherry', 'apple'])
print(np.sort(arr5))

arr6 = np.array([[3, 2, 4], [5, 0, 1]])
print(np.sort(arr6))

#SearchSorted
arr = np.array([6, 7, 8, 9])
v= np.searchsorted(arr, 14)
print(v)  

#FilteringArray

arr8=np.array([1,2,3,4,5])
filter_arr=[True,False,True,False,True]
r=arr8[filter_arr]
print(r)

arr9=np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17])
filter_arr1= arr9 %2 == 0
newarr2=arr9[filter_arr1]
print(filter_arr1)
print(newarr2)        

arr10=np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17])
filter_arr2= arr10>10
newarr3=arr9[filter_arr2]
print(filter_arr2)
print(newarr3)    
