import matplotlib.pyplot as plt
fruits = ["Apple", "Banana", "Cherry", "Date", "Elderberry", "Fig", "Grape", "Honeydew", "Kiwi", "Lemon", "Mango", "Nectarine"]
quantity = [7, 2, 11, 4, 9, 1, 6, 12, 3, 8, 5, 10]

plt.figure(figsize=(12, 6))
plt.bar(fruits, quantity, color = ['lightblue', 'blue', 'purple', 'red', 'black', 'orange', 'green', 'pink', 'brown', 'yellow', 'cyan', 'magenta'])
plt.title("Fruit consumption")
plt.xlabel("Fruit type")
plt.ylabel("Quantity")
plt.show()