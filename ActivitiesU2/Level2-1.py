import matplotlib.pyplot as plt

months = [1, 2, 3, 4, 5, 6]
product1 = [11.0, 11.0, 13.0, 15.0, 18.0, 22.0]
product2 = [14.0, 11.0, 14.0, 18.0, 14.0, 23.0]

plt.figure(figsize=(6,4))
plt.plot(months, product1, label="Apples")
plt.plot(months, product2, label="Oranges", color="orange")
plt.ylabel("Quantity")
plt.xlabel("Months")
plt.title("Sales by Month")
plt.legend()
plt.show()
