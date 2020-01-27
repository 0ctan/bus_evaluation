import pandas as pd
import sys
import re

args = sys.argv

file = args[1]
print(file)

df = pd.read_csv(file)
print(df.shape)
print(df.isnull().sum())
df.dropna(axis=0,inplace=True)

print(df.shape)
print(df.isnull().sum())

df.to_csv("data/tmp.csv", index=False)


with open("data/tmp.csv", "r") as f:
    s=f.read()


# timeを計算可能な形式に
s = s.replace('-', ',')
s = s.replace('T', ',')
s = s.replace(':', ',')
s = re.sub(r'\....Z', '', s)


with open("data/clean.csv", "w") as f:
    f.write(s)
