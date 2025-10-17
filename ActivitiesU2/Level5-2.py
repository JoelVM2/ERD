import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

sales_data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
    'Sales': [150, 200, 180, 250, 220, 280],
    'Region': ['North', 'South', 'North', 'East', 'West', 'East'],
    'Profit': [50, 60, 55, 70, 65, 80]
}
df_dashboard = pd.DataFrame(sales_data)
np.random.seed(42)
df_dashboard['Marketing_Spend'] = np.random.randint(10, 50, size=len(df_dashboard))
fig, axes = plt.subplots(2, 2, figsize=(18, 12))
fig.suptitle('Sales', fontsize=20)
axes[0, 0].plot(df_dashboard['Month'], df_dashboard['Sales'], marker='o', linestyle='-', color='b')
axes[0, 0].set_title('Monthly Sales', fontsize=14)
axes[0, 0].set_xlabel('Month')
axes[0, 0].set_ylabel('Sales (€)')
axes[0, 0].grid(True)
axes[0, 1].hist(df_dashboard['Sales'], bins=5, edgecolor='black', color='lightgreen')
axes[0, 1].set_title('Sale distribution', fontsize=14)
axes[0, 1].set_xlabel('Sales (€)')
axes[0, 1].set_ylabel('Frequency')
axes[0, 1].grid(axis='y')
axes[1, 0].scatter(df_dashboard['Marketing_Spend'], df_dashboard['Sales'], color='purple')
axes[1, 0].set_title('Sales vs. Marketing spending', fontsize=14)
axes[1, 0].set_xlabel('Marketing spending (€)')
axes[1, 0].set_ylabel('Sales (€)')
axes[1, 0].grid(True)
region_sales = df_dashboard.groupby('Region')['Sales'].sum()
axes[1, 1].pie(region_sales, labels=region_sales.index, autopct='%1.1f%%', startangle=90, colors=['gold', 'lightcoral', 'skyblue', 'lightgreen'])
axes[1, 1].set_title('Region sales', fontsize=14)
plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.show()
