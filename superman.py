
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(12, 18, 0.01)
y = -abs(x) + 21
plt.plot(x, y, '-r')

x = np.arange(-18, -12, 0.01)
y = -abs(x) + 21
plt.plot(x, y, '-r')

x = np.arange(-12, 12, 0.01)
y = np.full(np.shape(x), 9)
plt.plot(x, y, '-r')

x = np.arange(-18, 18, 0.01)
y = abs(x) - 15
plt.plot(x, y, '-r')

x = np.arange(-11, -8, 0.01)
y = np.full(np.shape(x), 7)
plt.plot(x, y, '-r')

x = np.arange(-1, 0, 0.01)
y = np.full(np.shape(x), 7)
plt.plot(x, y, '-r')

x = np.arange(7, 9, 0.01)
y = np.full(np.shape(x), 7)
plt.plot(x, y, '-r')

x = np.arange(-15, -11, 0.01)
y = -abs(x) + 18
plt.plot(x, y, '-r')

x = np.arange(12, 15, 0.01)
y = -abs(x) + 18
plt.plot(x, y, '-r')

x = np.arange(-15, -13, 0.01)
y = abs(x) - 12
plt.plot(x, y, '-r')

x = np.arange(-9, -6, 0.01)
y = abs(x) - 12
plt.plot(x, y, '-r')

x = np.arange(-4, 4, 0.01)
y = abs(x) - 12
plt.plot(x, y, '-r')

x = np.arange(11, 15, 0.01)
y = abs(x) - 12
plt.plot(x, y, '-r')

x = np.arange(0, 6, 0.01)
y = -(1 / 3 * x) ** 2 + 7
plt.plot(x, y, '-r')

x = np.arange(6, 12, 0.01)
y = np.full(np.shape(x), 3)
plt.plot(x, y, '-r')

y = np.arange(3, 6, 0.01)
x = np.full(np.shape(y), 12)
plt.plot(x, y, '-r')

x = np.arange(-200, -1, 0.01)
y = np.sqrt(x + 5) + 5
plt.plot(x, y, '-r')

x = np.arange(-4, 4, 0.01)
y = (x / 4) ** 2 - 9
plt.plot(x, y, '-r')

x = np.arange(7, 8, 0.01)
y = 2 * np.sqrt(-(x - 8)) + 5
plt.plot(x, y, '-r')

x = np.arange(8, 9, 0.01)
y = 2 * x - 11
plt.plot(x, y, '-r')

x = np.arange(-200, -8, 0.01)
y = 6 * np.sqrt((x + 13) / 5) + 1
plt.plot(x, y, '-r')

x = np.arange(-6, 0, 0.01)
y = -((x + 3) / 3) ** 2 - 5
plt.plot(x, y, '-r')

x = np.arange(-6, 0, 0.01)
y = -((x + 3) / 3) ** 2 - 5
plt.plot(x, y, '-r')

x = np.arange(-9, -1, 0.01)
y = ((x + 1) / 8) ** 2 - 4
plt.plot(x, y, '-r')

x = np.arange(-1, 0, 0.01)
y = np.full(np.shape(x), -4)
plt.plot(x, y, '-r')

x = np.arange(0, 1000, 0.01)
y = np.sqrt(-(x - 6) / 6) - 5
plt.plot(x, y, '-r')

x = np.arange(0, 1000, 0.01)
y = -np.sqrt(-(x - 6) / 6) - 5
plt.plot(x, y, '-r')

x = np.arange(-1000, 0, 0.01)
y = -3 / 5 * np.sqrt(5 * (x + 5)) + 5
plt.plot(x, y, '-r')

x = np.arange(0, 1000, 0.01)
y = 3 / 5 * np.sqrt(-2.27 * (x - 11)) - 1
plt.plot(x, y, '-r')

plt.show()
