import pandas as pd
import numpy as np

a = pd.Series([2,3,-2,1])
print(a)

print(a.values)
print(a.index)
print(a[0])

a[0] = 10
print(a)

print(a[1:])

b = pd.Series([2,3,-2,1],index=["d","b","a","c"])
print(b)

print(b.values)
print(b.index)
print(b['d'])

b['d'] = 6
print(b)

print(b[['a','b','c']])
print(b[0:3])
print(b[::2])
print(b[b>0])
print(b*2)
print(np.power(b,2))

data = {"KTM":29,"PKR":24,"BRJ":33}
c = pd.Series(data)
print(c)

cities = ["BRJ","KTM","PKR","ITA"]
d = pd.Series(data,index=cities)
print(d)

print(pd.isnull(d))
print(pd.notnull(d))
print(d.isnull())

print(c)
print(d)

print(c + d)
print(d * 2)

c.name = "temperatures"
c.index.name = "city"
print(c)

data = {'city':['KTM','KTM','PKR','PKR','BRJ','BRJ'],
       'day':['SUN','MON','SUN','MON','SUN','MON'],
       'temp':[23,22,25,26,30,31]}
df = pd.DataFrame(data)
print(df)

print(pd.DataFrame(data,columns=['day','city','temp']))

df2 = pd.DataFrame(data,columns=['day','city','temp','humidity'],
            index=['one','two','three','four','five','six'])
print(df2)

print(df.columns)
print(df.city)
print(df['city'])
print(df2.city)
print(df2['city'])
print(df2.loc['three'])
print(df2.iloc[0])

df2['humidity'] = np.random.randint(2,10,6)
print(df2)

df2['capital'] = df2['city'] == 'KTM'
print(df2)

del df2['capital']
print(df2.columns)
print(df2)

print(df2.drop('one'))
print(df2)

df2.drop('one',inplace=True)
print(df2)

print(df2.drop(['two','six']))
print(df2.drop(columns='day'))
print(df2.drop(columns=['day','temp']))
print(df2)

df2.index.name = 'day-count'
df2.columns.name = 'details'
print(df2)

print(df.values)

df3 = pd.Series(np.arange(4),index=['a','b','c','d'])
print(df3)

print(df3['b'])
print(df3[1])
print(df3[2:4])
print(df3[['b','a','d']])
print(df3[[1,3]])
print(df3[df3<2])

data = pd.DataFrame(np.arange(16).reshape((4,4)),
                   index=['KTM','PKR','BRJ','ITA'],
                   columns=['one','two','three','four'])
print(data)

print(data['two'])
print(data[['three','one']])
print(data[:2])
print(data[data['three']>5])
print(data > 5)

data[data>5]=0
print(data)

print(data.loc['KTM',['two','three']])
print(data.loc[['KTM','BRJ'],['one','two','three']])
print(data.loc['KTM'])
print(data['one'])

print(data.iloc[0])
print(data.iloc[:,0])
print(data.iloc[:,[0,3]])
print(data.iloc[:,1:3])
print(data.iloc[[0,3],[1,2]])
print(data.iloc[[1,3],:])
print(data.iloc[:2,:2])

df1 = pd.DataFrame(np.arange(9).reshape((3,3)),
                   columns=list('bcd'),
                   index=['Ohio','Texas','Colorado'])
print(df1)

df2 = pd.DataFrame(np.arange(12).reshape((4,3)),
                   columns=list('bde'),
                   index=['Utah','Ohio','Texas','Oregon'])
print(df2)

print(df1 + df2)

df = pd.DataFrame(np.random.randint(10,20,(4,3)),
                 columns=list("bde"),
                 index=['Utah','Ohio','Texas','Oregon'])
print(df)

print(np.sqrt(df))
print(df)

print(df.sum())
print(df.sum(axis=1))

print(df['b'].max())
print(df['b'].min())
print(df['b'].mean())

print(df['b'])
print(df['b'].idxmax())
print(df['b'].idxmin())
print(df['b'].value_counts())
print(df['b'].unique())

print(df.iloc[0])
print(df.iloc[0].sum())

s = pd.Series(range(5),index=['z','c','y','a','b'])
print(s)

print(s.sort_index())

df = pd.DataFrame(np.arange(8).reshape((2,4)),
                 index=['three','one'],
                 columns=['d','a','b','c'])
print(df)

print(df.sort_index())
print(df.sort_index(axis=1))
print(df.sort_index().sort_index(axis=1))
print(df.sort_index(axis=1,ascending=False))

print(s)
print(s.sort_values())

print(df)
print(df.sort_values(by="b"))
print(df.sort_values(by="b",ascending=False))