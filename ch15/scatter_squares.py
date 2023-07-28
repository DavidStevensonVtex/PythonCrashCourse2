import matplotlib.pyplot as plt

plt.style.use('seaborn')
fig, ax = plt.subplots()
input_values = [ 1, 2, 3, 4, 5 ]
squares = [ 1, 4, 9, 16, 25 ]
ax.scatter(input_values, squares)

plt.show()