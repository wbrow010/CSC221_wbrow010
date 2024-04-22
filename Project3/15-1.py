import matplotlib.pyplot as plt

numbers = [1, 2, 3, 4, 5]

cubes = [1, 8, 27, 64, 125]

plt.style.use('bmh')
fig, ax = plt.subplots()

ax.scatter(numbers, cubes)
ax.set_title("15-1 - Cubes")
ax.set_xlabel('Number')
ax.set_ylabel('Cube of Number')

plt.show()