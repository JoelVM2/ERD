import random
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


grades = [random.randint(4, 10) for _ in range(50)]
plt.figure(figsize=(10, 6))
sns.histplot(data=grades, kde=True)
plt.title('Students per grade')
plt.xlabel('Grades')
plt.ylabel('Grade Range')
plt.grid(True)
plt.show()
