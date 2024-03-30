import matplotlib.pyplot as plt

U = 20
A = 5

time_values = list(range(0, 21))
vilocity_values = [U + A * t for t in time_values]

plt.plot(time_values, vilocity_values)
plt.title("Vilocity vs Time")
plt.xlabel("Time")
plt.ylabel("Vilocity")

plt.grid(True)
plt.show()
