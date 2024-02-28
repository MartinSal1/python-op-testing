import matplotlib
import matplotlib.pyplot as plt

print("--")

x_coordinates = []
y_coordinates = []

filename = "plotting_file/x_y_coordinates.txt"
# method1
""" try:
    with open(filename, "r") as file:
        for line in file:
            line = line.strip()# strip whitespace
            x, y = line.rstrip(',').split()
            print(x, y)
            x_coordinates.append(float(x))   
            y_coordinates.append(float(y))   
except FileNotFoundError:
    print("file not found") """
# method2
readfile = open(filename)
data = readfile.read().split("\n")

for line in data:
    val = line.split(',')
    x_coordinates.append(int(val[0]))
    y_coordinates.append(int(val[1]))

#plot
plt.plot(x_coordinates, y_coordinates)  # Sample plot
plt.show()

