import numpy as np
import pandas as pd

# Task 1
arr = np.array([
    [10, 20, 30, 40],
    [15, 25, 35, 45],
    [27, 29, 37, 48],
    [32, 33, 39, 50]
])
print(arr)

# Slicing Questions
print(arr[0])
print(arr[3])
print(arr[0:2, 0:3])
print(arr[1])
print(arr[1:4, 1:3])

# Masking
print(arr[arr > 30])
print(arr[arr % 2 == 0])

arr[arr < 25] = 0
print(arr)

x = arr[(arr >= 20) & (arr <= 40)]
print(x)

arr[arr[:, -1] > 45, -1] = -1
print(arr)

# Task 2
data_labels_1 = ['Biratnagar', 'Kathmandu', 'Lalitpur', 'Pokhara', 'Narayangarh']
data_values_1 = [200000, 1600000, 600000, 500000, 350000]
series_numpy_array_1 = np.array([200000, 1600000, 600000, 500000, 350000])
dict2 = {
    'Biratnagar': 200000,
    'Kathmandu': 1600000,
    'Lalitpur': 600000,
    'Pokhara': 500000,
    'Narayangarh': 350000
}

cities_population = pd.Series(
    data=[200000, 1600000, 600000, 500000, 350000],
    index=['Biratnagar', 'Kathmandu', 'Lalitpur', 'Pokhara', 'Narayangarh']
)
print(cities_population)

s1 = pd.Series(data_labels_1)
print(s1)

s2 = pd.Series(data_labels_1)
print(s2)

s3 = pd.Series(data_values_1, index=data_labels_1)
print(s3)

s4 = pd.Series(series_numpy_array_1, index=data_labels_1)
print(s4)

s5 = pd.Series(dict2)
print(s5)

# Task 3
print(cities_population.index)

cities_population_2 = pd.Series(
    index=['Bhaktapur', 'Kathmandu', 'Lalitpur', 'Pokhara', 'Butwal'],
    data=[150000, 1600000, 600000, 500000, 300000]
)
print(cities_population_2)

print(cities_population + cities_population_2)

serial_no = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
subjects = ['ENG', 'NEP', 'MAT', 'SCI', 'COM']
students = ['RAM', 'SHYAM', 'GITA', 'HARI', 'SITA', 'SUSHILA', 'RAMESH', 'SUBODH', 'ANIL', 'RUPA']
marks = [
    [57, 34, 93, 84, 54],
    [48, 92, 89, 64, 66],
    [64, 75, 38, 84, 55],
    [47, 90, 82, 37, 45],
    [93, 70, 53, 76, 45],
    [63, 33, 53, 72, 68],
    [34, 42, 43, 84, 62],
    [69, 67, 50, 94, 59],
    [33, 51, 68, 33, 57],
    [91, 60, 37, 44, 41]
]

df1 = pd.DataFrame(marks, columns=subjects, index=students)
print(df1)

nep_pass = df1[df1['NEP'] >= 40]
print(nep_pass.index)

first_div_sci = df1[df1['SCI'] >= 70]
print(first_div_sci.index)