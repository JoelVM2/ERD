import matplotlib.pyplot as plt

labels = 'Chrome', 'Firefox', 'Safari', 'ALtres'
sizes = [65, 20, 10, 5]

fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct='%1.1f%%')