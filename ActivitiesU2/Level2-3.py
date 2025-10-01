import random
import numpy as np
import matplotlib.pyplot as plt

grades = [random.randint(0, 10) for _ in range(30)]
bins = [0, 2, 4, 6, 8, 10]
style = {'facecolor': 'none', 'edgecolor': 'C0', 'linewidth': 2}
fig, ax = plt.subplots()
ax.hist(grades, bins=bins, **style)
ax.plot(grades, [0]*len(grades), 'd')
bin_centers = [(bins[i] + bins[i+1]) / 2 for i in range(len(bins)-1)]
ax.set_xticks(bin_centers)
ax.set_xticklabels(["0-2", "2-4", "4-6", "6-8", "8-10"])
ax.set_ylabel('Students per grade')
ax.set_xlabel('Grade Range')

plt.show()
