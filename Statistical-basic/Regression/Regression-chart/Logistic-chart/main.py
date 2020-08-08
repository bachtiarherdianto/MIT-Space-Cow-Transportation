import numpy as np
import matplotlib.pyplot as plt


x = np.arange(-5.0, 5.0, 0.1)
y = 1 - 4 / (1 + np.power(3, x - 2))
plt.style.use('dark_background')
plt.title('Logistic Regression Chart')
plt.plot(x, y, 'r')
plt.text(2.5, -2.5, r'$y = 1 + {\frac {4}{1 + 3 ^ (X - 2)}}$')
plt.ylabel('Dependent Variable')
plt.xlabel('Independent Variable')
plt.show()
