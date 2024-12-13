import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import cm
from cycler import cycler
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

def load_data(file_path):
    # Load data using pandas
    data = pd.read_excel(file_path, header=None)
    return data.values

# Load data from your file
file_path = 'dos-1a-1.xls'  # Your file path here
data = load_data(file_path)

# Extract x and y values
x = data[:, 0]
ys = [data[:, i] for i in range(3, 19)]  # From y1 to y16

# Create a figure
plt.figure(figsize=(8, 18))

# Generate a color map and create a color cycler
num_lines = len(ys)
color_map = plt.get_cmap('viridis')  # You can choose any other appealing colormap like 'plasma', 'inferno', etc.
colors = color_map(np.linspace(0, 1, num_lines))
plt.gca().set_prop_cycle(cycler('color', colors))

for i, y in enumerate(ys):
    plt.plot(x, y + 0.1*i, linewidth=3)  # Adjust y if needed for separation

#plt.legend()
plt.xlim(-9, 0)
plt.tick_params(axis='x', which='both', bottom=True, top=False, labelbottom=False)
# 隐藏横坐标和纵坐标的刻度
#plt.xticks([])
plt.yticks([])
#plt.legend()
#plt.xlabel('Energy (nm)')
#plt.ylabel('Dos')

# Save the figure
plt.savefig('pdos-atoms.png', format='png')
plt.close()
