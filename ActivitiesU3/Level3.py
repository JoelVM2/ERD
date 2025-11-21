
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv("ActivitiesU3\grades.csv")
print("File loaded successfully:\n")
print(df)

df["Average"] = df[["Mathematics", "Catalan", "English"]].mean(axis=1)

df.plot(x="Name", y="Average", kind="bar", legend=False)
plt.title("Average Grade per Student")
plt.xlabel("Name")
plt.ylabel("Average")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

options = ["I like Python", "I prefer JavaScript", "I'm indifferent"]
votes = [45, 30, 25]

plt.pie(votes, labels=options, autopct="%1.1f%%")
plt.title("Survey Results")
plt.tight_layout()
plt.show()

weeks = ["Week1", "Week2", "Week3", "Week4"]

product_A = [120, 150, 130, 160]
product_B = [80, 90, 100, 95]
product_C = [200, 210, 190, 220]

plt.plot(weeks, product_A, label="Product A")
plt.plot(weeks, product_B, label="Product B")
plt.plot(weeks, product_C, label="Product C")

plt.title("Weekly Sales per Product")
plt.xlabel("Weeks")
plt.ylabel("Sales")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

sns.boxplot(data=df[["Mathematics", "Catalan", "English"]])
plt.title("Grade Distribution by Subject")
plt.ylabel("Grade")
plt.tight_layout()
plt.show()
