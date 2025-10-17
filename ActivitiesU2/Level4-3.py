import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('ActivitiesU2/sales_data.csv')
fig, ax = plt.subplots(1, 2)
plt.figure(figsize=(20,4),dpi=90)
plt.xlabel('Monthly sales', fontsize=12)
plt.ylabel('Quantity', fontsize=12)
plt.bar(df.Month,df.Sales)
fig.set_figwidth(19)
ax[0].plot(df.Month,df.Sales)
ax[1].hist(df.Sales, bins=10, edgecolor='black', color='lightgreen')
ax[1].set_xlabel('Ventas', fontsize=12)
ax[1].set_ylabel('Frecuencia', fontsize=12)
ax[1].set_title('Distribución de las ventas')
ax[1].grid(axis='y', alpha=0.5, linestyle='--')
plt.show()