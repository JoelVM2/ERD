import matplotlib.pyplot as plt
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
temperatures = [11.0, 11.0, 13.0, 15.0, 18.0, 22.0, 24.0, 24.0, 22.0, 18.0, 14.0, 12.0]
plt.plot(months, temperatures, marker="o", color="red")
plt.title("Temperatures per month")
plt.xlabel("Months")
plt.ylabel("Temperatures")
plt.show()