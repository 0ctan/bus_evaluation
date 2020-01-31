import pandas as pd
import csv
import datetime

file = "data/keiiku.csv"

f = pd.read_csv(file, header=None)
# 絞り込み
use = f[[3,8,9]]
use[9] = pd.to_timedelta(use[9])
use[9] = use[9].dt.total_seconds()

weekday_bin = use.groupby([3,8])
# print(weekday_bin.groups)
mean = weekday_bin.mean()
print(mean.loc[0,'A1']) # 月曜のA1便の平均遅延

