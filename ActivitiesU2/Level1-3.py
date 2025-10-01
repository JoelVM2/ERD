import matplotlib.pyplot as plt

labels = 'Chrome', 'Firefox', 'Safari', 'Others...'
sizes = [65, 20, 10, 5]
explode = (0.1, 0, 0, 0)
fig, ax = plt.subplots()
ax.pie(sizes, explode=explode, labels=labels, 
autopct='%1.1f%%',shadow=True, startangle=90)
plt.show()