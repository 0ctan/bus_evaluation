import pandas as pd
import sys

args = sys.argv

file = args[1]
print(file)

df = pd.read_csv(file)
print(df.shape)
print(df.isnull().sum())
df.dropna(axis=0,inplace=True)

print(df.shape)
print(df.isnull().sum())

df.to_csv("data/clean.csv", index=False)