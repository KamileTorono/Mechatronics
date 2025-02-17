#!usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt

# Define the equation x^2 + 5y/4 - (sqrt|x|)^2 = 1
# Solving for y: y = (4/5) * (1 + (sqrt(|x|))^2 - x^2)
def equation_y(x):
    return (4/5) * (1 + np.sqrt(np.abs(x))**2 - x**2)

# Generate x values
x_vals = np.linspace(-2, 2, 400)  # X values from -2 to 2

# Compute y values
y_vals = equation_y(x_vals)

# Plot the graph
plt.figure(figsize=(8,6))
plt.plot(x_vals, y_vals, label=r'$x^2 + \frac{5y}{4} - (\sqrt{|x|})^2 = 1$')

# Add labels and title
plt.title('Graph of the equation: $x^2 + \\frac{5y}{4} - (\\sqrt{|x|})^2 = 1$')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend()

# Show the plot
plt.show()
