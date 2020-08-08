import numpy as np
import matplotlib.pyplot as plt


x = np.arange(-5.0, 5.0, 0.1)
y = np.log(x)
plt.style.use('dark_background')
plt.title('Logarithmic Regression Chart')
plt.plot(x, y, 'r')
plt.text(3, 0, r'$y = \log(X)$')
plt.ylabel('Dependent Variable')
plt.xlabel('Independent Variable')
plt.show()
