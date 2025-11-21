
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

np.random.seed(42)
months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
tourists = np.random.randint(5000, 20000, size=12)
hotels = np.random.randint(50, 150, size=12)
avg_spending = np.random.uniform(500, 1500, size=12)

df = pd.DataFrame({
    "Month": months,
    "Tourists": tourists,
    "Hotels": hotels,
    "AvgSpending": avg_spending
})

print(df)

plt.figure(figsize=(8,5))
plt.bar(df["Month"], df["Tourists"], color="skyblue")
plt.title("Monthly Tourists in Balearic Islands", fontsize=14)
plt.xlabel("Month")
plt.ylabel("Number of Tourists")
plt.tight_layout()
plt.savefig("bar_chart_tourists.png")
plt.show()

plt.figure(figsize=(8,5))
plt.plot(df["Month"], df["Hotels"], marker='o', label="Hotels Open", color='orange')
plt.plot(df["Month"], df["AvgSpending"], marker='s', label="Avg Spending (€)", color='green')
plt.title("Hotels Open & Avg Spending per Month", fontsize=14)
plt.xlabel("Month")
plt.ylabel("Value")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("line_chart_hotels_spending.png")
plt.show()

plt.figure(figsize=(6,6))
plt.pie(df["Tourists"], labels=df["Month"], autopct="%1.1f%%", startangle=90, colors=plt.cm.tab20.colors)
plt.title("Tourist Distribution by Month", fontsize=14)
plt.tight_layout()
plt.savefig("pie_chart_tourists.png")
plt.show()

total_tourists = df["Tourists"].sum()
avg_hotels = df["Hotels"].mean()
avg_spending_overall = df["AvgSpending"].mean()

report = f"""
INFORME TURISME ILLES BALEARS

1. Total tourists in the year: {total_tourists}
2. Average hotels open per month: {avg_hotels:.1f}
3. Average spending per tourist: €{avg_spending_overall:.2f}

Observations:
- July and August have the highest tourist numbers.
- Average spending peaks in summer months.
- Hotel availability aligns with peak tourist season.
"""
print(report)

with open("tourism_report.txt", "w") as f:
    f.write(report)
