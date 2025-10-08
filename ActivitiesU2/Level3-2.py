import seaborn as sns
import matplotlib.pyplot as plt

# A más horas de estudio mejores notas
study_time = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
grades = [4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0, 8.5, 9.0]
sns.set(style='whitegrid')
sns.scatterplot(x=study_time, y=grades)
plt.xlabel("Study time")
plt.xlabel("Grades")
plt.show()