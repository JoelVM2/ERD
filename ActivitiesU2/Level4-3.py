import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('ActivitiesU2/sales_data.csv')
#Hacer etiquetas mas pequeñas y añadir etiquetas de cardinalidad
plt.figure(figsize=(16,4))
plt.bar(df.Month,df.Sales)
plt.show()