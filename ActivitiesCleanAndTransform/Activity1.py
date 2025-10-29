import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Bob","Charlie",None, "Diana"],
    "Age": [20, None, 21, 19, None, 22],
    "Grade": [8.8, None, 9.2, 7.9,None, 8.50]
}
df = pd.DataFrame(data)
df["Age"].fillna(df["Age"].mean(), inplace=True)
df["Grade"].fillna(0, inplace=True)
df["Age"] = df["Age"].astype(str)


df_without_blank = df.dropna()
df_no_duplicate = df_without_blank.drop_duplicates(subset=["Name"])
print("Data:\n", df_no_duplicate)
