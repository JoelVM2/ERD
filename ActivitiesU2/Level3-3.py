import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    "Student": ["Anna", "Marc", "Laura", "David", "Júlia"],
    "Mathematics": [8.5, 6.0, 9.0, 5.5, 7.5],
    "History": [7.0, 8.5, 9.5, 6.0, 8.0],
    "English": [9.0, 7.0, 8.5, 6.5, 8.0]
}

df = pd.DataFrame(data)

df_long = df.melt(
    id_vars="Student",
    value_vars=["Mathematics", "History", "English"],
    var_name="Subject",
    value_name="Grade"
)

sns.boxplot(x="Subject", y="Grade", data=df_long)
plt.show()
