import pandas as pd
df=pd.read_csv('Pandas/Dataset1.csv')
print(df)

print(df.dtypes)

print(df.columns)

print(df.iloc[0:5])

a=(df[df['Year']>2022])

print(a)

print(df.shape)

print(df.describe())

new_df = df.dropna()

print(new_df.to_string())

print(df.isnull().sum())

print(df.duplicated())

print(df.duplicated().sum())

print(df.duplicated(subset='Year').sum())

print(df.columns)

