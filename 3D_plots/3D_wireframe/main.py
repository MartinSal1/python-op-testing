import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import numpy as np
""" from mpl_toolkits.mplot3d import Axes3D  """
# Data
""" x = np.array([1, 2, 3, 4, 5])
y = np.array([10, 20, 15, 25, 30])
z = np.zeros_like(x)

dx = np.ones_like(x)
dy = np.ones_like(y)
dz = np.array([5, 10, 7, 15, 20])
 """
# 3D Bar graph
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x,y,z = axes3d.get_test_data(0.05)
ax.plot_wireframe(x, y, z, rstride=2, cstride=2)
# Labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()

""" import plotly.graph_objects as go
import numpy as np

# Generate random data
x = np.linspace(-5, 5, 101)
y = np.linspace(-5, 5, 101)
x, y = np.meshgrid(x, y)
z = np.random.rand(101, 101)  # Random heights for each point

# Create a 3D wireframe plot
fig = go.Figure(data=[go.Surface(z=z, x=x, y=y, colorscale='Viridis')])
fig.update_layout(scene=dict(
                    xaxis_title='X',
                    yaxis_title='Y',
                    zaxis_title='Z'),
                    )
fig.show() """