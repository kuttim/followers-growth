import pandas as pd

data = pd.read_csv("data/2016.csv")

df = pd.DataFrame(data)

df = df.replace('[Mæ(=)]', '', regex=True)
print(df)

df.to_csv("data/2022.csv", index=False)
