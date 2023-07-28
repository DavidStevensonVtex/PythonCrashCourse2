import matplotlib.pyplot as plt

plt.style.use('seaborn')
fig, ax = plt.subplots()
x_values = [ 1, 2, 3, 4, 5 ]
y_values = [ 1, 4, 9, 16, 25 ]
ax.scatter(x_values, y_values)

plt.show()