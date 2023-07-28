import matplotlib.pyplot as plt

input_values = [ 1, 2, 3, 4, 5 ]
squares = [ 1, 4, 9, 16, 25 ]

plt.style.use('seaborn')
# mpl_squares.py:6: MatplotlibDeprecationWarning: The seaborn styles shipped by Matplotlib are deprecated since 3.6, 
# as they no longer correspond to the styles shipped by seaborn. However, they will remain available as 
# 'seaborn-v0_8-<style>'. Alternatively, directly use the seaborn API instead.

fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=3)

# Set chart title and label axes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick mark
ax.tick_params(axis='both', labelsize=14)

plt.show()