import pandas as pd
import numpy as np

df = pd.read_csv("./Datasets/Waterdataset.csv")

df = df.astype(float)

df.rename(columns={
    "ph": "pH",
    "Hardness": "hardness",
    "Solids": "solids"
}, inplace=True)

print(df.head(7))

print(df.tail(7))

print(df.loc[0:200, df.columns[:4]])

print(df.iloc[0:201, 0:4])

print(df.columns)

print(df.shape)

print(df.dtypes)

print(df.describe())

print(df.isnull().sum())

for col in df.columns[:-1]:
    df[col] = df[col].replace(0, np.nan)


df.fillna(df.mean(), inplace=True)

df = df.drop(df.columns[2], axis=1)

df = df.iloc[3:]

filtered = df[['Sulfate', 'Conductivity', 'Turbidity']]
print(filtered.head())

df = df.drop_duplicates()

df = df.dropna()

print(df[df['Conductivity'] > 300])

print(df[df['pH'] < 7])

print(df.sort_values(by='pH'))

print(df.sort_values(by='Turbidity', ascending=False))


pivot = df.pivot_table(values='Turbidity',index='Potability',aggfunc='mean')
print(pivot)

df.to_csv("Datasets/cleaned_water_dataset.csv", index=False)

