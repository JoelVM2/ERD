import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('ActivitiesU2/sales_data.csv')
fig, ax = plt.subplots()
plt.figure(figsize=(20,4),dpi=90)
plt.xlabel('Monthly sales', fontsize=12)
plt.ylabel('Quantity', fontsize=12)
plt.bar(df.Month,df.Sales)
fig.set_figwidth(19)
ax.plot(df.Month,df.Sales)
plt.show()

# Falta histograma