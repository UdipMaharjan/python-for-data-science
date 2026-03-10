import pandas as pd
df=pd.read_csv('dataset1.csv')
sd=pd.read_excel('dataset2.xlsx')
rd=pd.read_json('dataset3.json')

print(df.to_string())

x=df.head(10)
print(x)

y=df.tail(10)
print(y)

print(df.info())

#Series

a=pd.Series([1,2,3,4,5], index=['a','b','c','d','e'])
print(a)
print(a.loc['a'])

b={1:"Cristiano", 2:"Lionel", 3:"Neymar"}
c=pd.Series(b)
print(c)

#DataFrames

data={"Names":["Ronaldo","Messi","Neymar"], "Goals":[1007,978,545]}
df=pd.DataFrame(data, index=[1,2,3])
print(df)
print(df.loc[1])