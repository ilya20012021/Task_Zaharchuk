from pyarrow import csv
from pandas import *
df = csv.read_csv("D:/traffic_security.csv").to_pandas()
df1 = df.iloc[::,1]
b = []
for i in range(len(df1)):
  t = df1[i]
  r = list(t)
  v = []
  for j in r:
    if j != ".":
      v.append(j)
    else:
      break
  z = "".join(v)
  b.append(z)
  v.clear()


c = set(b)
d = list(c)
m = []
for i in d:
    x = b.count(i)
    m.append(x)

df2 = DataFrame({"first_num_ip":d,
                 "counts":m})

df2 = df2.loc[df2["first_num_ip"].isin(["12","13","14"])]

df3 = df2.loc[df2["counts"] == df2["counts"].max()]
df4 = list(df3["first_num_ip"])[0]

df5 = DataFrame({"First_num_ip":b})
df6 = df5.loc[df5["First_num_ip"] == df4]
df7 = []
for i in df6.index:
    df7.append(i)

df8 = df.loc[df7]
df9 = df8.loc[df8.iloc[::,4] == df8.iloc[::,4].max()]
df10 = list(df9.iloc[::,1])[0]
print(df10)