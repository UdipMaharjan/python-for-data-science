import matplotlib.pyplot as plt
import numpy as np
x=[3,5,7,8]
y=[1,5,6,7]
plt.plot(x,y)
plt.show()

r=["Apples","Bananas","Oranges"]
z=[10,20,15]
plt.figure()
plt.bar(r, z, color=['red', 'yellow', 'orange'], width=0.5  )
plt.xlabel("Fruits")
plt.ylabel("Quantity")
plt.title("Fruit Quantity")
plt.show()

n=["A","B","C","D"]
s=[5,7,3,9]
plt.barh(n, s, color=['blue', 'green', 'cyan', 'magenta'])
plt.xlabel("Scores")
plt.ylabel("Names")
plt.title("Horizontal Bar Chart")
plt.show()

v = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
m = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
colors = np.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100])
plt.scatter(v, m, c=colors, cmap='viridis')
plt.colorbar()
plt.show()

g = np.arange(10)
k = np.random.randint(1, 20, 10)
colors = np.random.rand(10)
plt.scatter(g, k, c=colors)
plt.show()