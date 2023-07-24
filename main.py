# Importing packages
import matplotlib.pyplot as plt
import numpy as np

# Creating a sample data for x-values
x = np.arange(2, 300, 4)

# Provide parameters of the linear function
m, c = 3, -2

# Calculating the y-values for all the x'-values
y = (m * x) + c

# Plotting the line created by the linear function
plt.plot(x, y, 'c', linewidth=2, label='y=3x-2')
plt.title('Linear Function (y=3x-2) plot')
plt.xlabel('x-values')
plt.ylabel('y-values')
plt.legend()
plt.show()