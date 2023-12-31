import matplotlib.pyplot as plt

plt.style.use('seaborn')
fig, ax = plt.subplots()
x_values = range(1,1001)
y_values = [ x**2 for x in x_values ]
ax.scatter(x_values, y_values, c = y_values, cmap = plt.cm.Blues, s = 10)

# Set the range for each axis.
ax.axis( [ 0, 1_100, 0, 1_100_000 ])

plt.savefig('squares_plot.png', bbox_inches='tight')