import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

animal_data = {
    'name': ['Giraffe', 'Lion', 'Crocodile', 'Monkey', 'Penguin', 'Panda'],
    'quantity': [3, 2, 5, 6, 3, 1]
}

df_animals = pd.DataFrame(animal_data)

df_animals.plot(x="name", y="quantity", kind="bar", legend=False)
plt.title("Quantity of animals")
plt.xlabel("Name")
plt.ylabel("Quantity")
plt.tick_params(axis='x', rotation=0)
plt.tight_layout()
plt.show()

prices = np.random.uniform(10, 20, 10)
days = np.arange(1, 11)

plt.plot(days, prices)
plt.title("Product price over 10 days")
plt.xlabel("Day")
plt.ylabel("Price")
plt.grid(True)
plt.tight_layout()
plt.show()

schedule_labels = ["Sleep", "Classes", "Free time", "Sports", "Study"]
schedule_hours = [56, 25, 20, 5, 10]

plt.pie(schedule_hours, labels=schedule_labels, autopct="%1.1f%%")
plt.title("Weekly schedule distribution")
plt.tight_layout()
plt.show()



random_numbers = np.random.randint(0, 21, 100)

plt.hist(random_numbers, bins=10, edgecolor='black')
plt.title("Histogram of random numbers (0–20)")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()
