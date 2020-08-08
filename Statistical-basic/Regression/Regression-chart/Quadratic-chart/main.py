import numpy as np
import matplotlib.pyplot as plt


x = np.arange(-5.0, 5.0, 0.1)
y = np.power(x, 2)
y_noise = 2 * np.random.normal(size= x.size)
y_data = y + y_noise
plt.style.use('dark_background')
plt.title('Quadratic Regression Chart')
plt.plot(x, y_data, 'bo')
plt.plot(x, y, 'r')
plt.text(3, 0, r'$y = x^2$')
plt.ylabel('Dependent Variable')
plt.xlabel('Independent Variable')
plt.show()