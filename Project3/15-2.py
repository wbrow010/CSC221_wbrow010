import matplotlib.pyplot as plt

numbers = range(1, 5001)

cubes = [number**3 for number in numbers]

plt.style.use('bmh')
fig, ax = plt.subplots()

ax.scatter(numbers, cubes)
ax.set_title("15-1 - Cubes")
ax.set_xlabel('Number')
ax.set_ylabel('Cube of Number')

plt.show()