#!/usr/bin/env python
import matplotlib.pyplot as plt
import numpy as np

# Data for the table
data = [['Row1-Col1', 'Row1-Col2', 'Row1-Col3', 'Row1-Col4'],
        ['Row2-Col1', 'Row2-Col2', 'Row2-Col3', 'Row2-Col4'],
        ['Row3-Col1', 'Row3-Col2', 'Row3-Col3', 'Row3-Col4']]

# Set up the figure and axis
fig, ax = plt.subplots()

# Hide the axes
ax.xaxis.set_visible(False) 
ax.yaxis.set_visible(False)
ax.set_frame_on(False)  # No box frame around the table

# Create the table
table = ax.table(cellText=data, loc='center')

# Auto-adjust the size of the cells
table.scale(1, 2)

# Display the plot
plt.show()