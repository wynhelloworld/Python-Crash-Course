import matplotlib.pyplot as plt

x = range(1, 1001)
y = [i**2 for i in x]

fig, ax = plt.subplots()
ax.scatter(x, y, c=y, cmap=plt.cm.Blues, s=10)
ax.axis([0, 1100, 0, 1_100_000])
ax.ticklabel_format(style='plain')

plt.show()
# plt.savefig('squares_plot.png', bbox_inches='tight')
