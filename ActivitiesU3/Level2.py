import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

students = ["Anna", "Marc", "Júlia", "Pau", "Laia", "Eric", "Nora", "David"]
math = [7, 5, 8, 6, 9, 4, 7, 6]
science = [6, 7, 5, 8, 9, 6, 7, 5]

df_grades = pd.DataFrame({
    "Student": students,
    "Math": math,
    "Science": science
})

print("DataFrame de notes:\n")
print(df_grades)

df_grades.plot(
    x="Student",
    kind="bar",
    stacked=True,
    title="Grades in Math and Science",
)

plt.ylabel("Grade")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()  

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
temp_min = [8, 7, 6, 7, 9, 10, 11]
temp_max = [15, 16, 14, 17, 18, 20, 19]

plt.plot(days, temp_min, label="Min temp")
plt.plot(days, temp_max, label="Max temp")

plt.title("Weekly Min & Max Temperatures")
plt.xlabel("Day")
plt.ylabel("°C")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

height = [150, 155, 160, 165, 170, 175, 180, 185]
weight = [45, 50, 55, 60, 65, 75, 80, 85]

plt.scatter(height, weight)
plt.title("Height vs Weight")
plt.xlabel("Height (cm)")
plt.ylabel("Weight (kg)")
plt.grid(True)
plt.tight_layout()
plt.show()

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

income =  [2000, 2100, 1900, 2200, 2300, 2400, 2500, 2450, 2300, 2200, 2100, 2000]
expenses = [1500, 1600, 1550, 1700, 1650, 1800, 1900, 1850, 1750, 1700, 1600, 1500]

x = np.arange(len(months))
width = 0.35

plt.bar(x - width/2, income, width, label="Income")
plt.bar(x + width/2, expenses, width, label="Expenses")

plt.title("Monthly Income vs Expenses")
plt.xlabel("Month")
plt.ylabel("€")
plt.xticks(x, months)
plt.legend()
plt.tight_layout()
plt.show()
