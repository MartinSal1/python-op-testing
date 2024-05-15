import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

X = [1, 2, 3, 4, 5]
Y = [2, 5, 3, 8, 9]
Z = np.array([[1,2,3,4,5],[3, 6, 2, 5, 7]])
Xx, Yy, Zz = [-1, -2, -3, -4, -5], [-2, -5, -3, -8, -9], [-2, -5, -3, -8, -9]

# ax.scatter(X, Y, Z, c='red', marker='o')#scatter issue.!!!!
ax.scatter(Xx, Yy, Zz, c='blue', marker='o')#scatter issue.!!!!

dx = np.ones(10)#[1,1,1,...]
dx = np.ones
ax.set_xlabel('x-axis')
ax.set_ylabel('y-axis')
ax.set_zlabel('z-axis')

ax.plot_wireframe(X, Y, Z)
plt.show()