import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Data
x = np.array([1, 2, 3, 4, 5])
y = np.array([10, 20, 15, 25, 30])
z = np.zeros_like(x)

dx = np.ones_like(x)
dy = np.ones_like(y)
dz = np.array([5, 10, 7, 15, 20])

# 3D Bar graph
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.bar3d(x, y, z, dx, dy, dz, color='b')

# Labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()

plt.show()