import numpy as np
import matplotlib.pyplot as plt


x = np.arange(-5.0, 5.0, 0.1)
y = 1*(x**3) + 1*(x**2) + 1*x + 3
y_noise = 20 * np.random.normal(size= x.size)
y_data = y + y_noise
plt.style.use('dark_background')
plt.title('Cubic Regression Chart')
plt.plot(x, y_data, 'bo')
plt.plot(x, y, 'r')
plt.text(1, -60, r'$y = x^3 + x^2 + x + 3$')
plt.ylabel('Dependent Variable')
plt.xlabel('Independent Variable')
plt.show()