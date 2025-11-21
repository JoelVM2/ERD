import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)
exercise_minutes = np.random.randint(0, 91, 30)
days = np.arange(1, 31)

plt.hist(exercise_minutes, bins=10, edgecolor='black')
plt.title("Distribution of Exercise Minutes (30 days)")
plt.xlabel("Minutes")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

plt.plot(days, exercise_minutes, marker='o')
plt.title("Exercise Minutes Over 30 Days")
plt.xlabel("Day")
plt.ylabel("Minutes")
plt.grid(True)
plt.tight_layout()
plt.show()

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

income = [2500, 2600, 2400, 2700, 2800, 3000, 3100, 3050, 2900, 2800, 2700, 2600]
expenses = [1800, 1900, 1750, 2000, 2100, 2200, 2300, 2250, 2100, 2050, 1950, 1850]

x = np.arange(len(months))
width = 0.6

plt.bar(x, income, width, label="Income", color="green")
plt.bar(x, expenses, width, label="Expenses", color="red", bottom=0)
plt.title("Monthly Family Budget")
plt.xlabel("Month")
plt.ylabel("€")
plt.xticks(x, months)
plt.legend()
plt.tight_layout()
plt.show()

savings = np.array(income) - np.array(expenses)
accumulated_savings = np.cumsum(savings)

plt.plot(months, accumulated_savings, marker='o', color='blue')
plt.title("Accumulated Savings Over the Year")
plt.xlabel("Month")
plt.ylabel("Accumulated Savings (€)")
plt.grid(True)
plt.tight_layout()
plt.show()

temp_min = [2, 3, 5, 8, 12, 15, 17, 16, 13, 9, 5, 3]
temp_max = [8, 10, 15, 18, 22, 26, 30, 29, 24, 18, 12, 9]

plt.plot(months, temp_min, label="Min Temperature", marker='o')
plt.plot(months, temp_max, label="Max Temperature", marker='o')
plt.title("Monthly Temperatures")
plt.xlabel("Month")
plt.ylabel("Temperature (°C)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

temp_mean = [(min_t + max_t)/2 for min_t, max_t in zip(temp_min, temp_max)]

plt.bar(months, temp_mean, color='orange')
plt.title("Average Monthly Temperature")
plt.xlabel("Month")
plt.ylabel("Temperature (°C)")
plt.tight_layout()
plt.show()
