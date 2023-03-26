# Поиск утечки данных из сети
Илья Москалёв

Переведём полученный дамп трафика в датафрейм Pandas:

``` python
from pyarrow import csv
import pandas as pd
df = csv.read_csv("traffic_security.csv").to_pandas()
df1 = df.iloc[::,1]
```

Получим ответ:

``` python
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

df2 = pd.DataFrame({"first_num_ip":d,
                 "counts":m})

df2 = df2.loc[df2["first_num_ip"].isin(["12","13","14"])]

df3 = df2.loc[df2["counts"] == df2["counts"].max()]
df4 = list(df3["first_num_ip"])[0]

df5 = pd.DataFrame({"First_num_ip":b})
df6 = df5.loc[df5["First_num_ip"] == df4]
df7 = []
for i in df6.index:
    df7.append(i)

df8 = df.loc[df7]
df9 = df8.loc[df8.iloc[::,4] == df8.iloc[::,4].max()]
list(df9.iloc[::,1])[0]
```

    '14.52.109.25'
