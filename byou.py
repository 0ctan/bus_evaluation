import pandas as pd

file = "data/evakeiiku.csv"
f = pd.read_csv(file, header=None)

f[9] = pd.to_timedelta(f[9])
f[9] = f[9].dt.total_seconds() # 時間を秒単位に変換
f.to_csv("evaluation/evakeiikubyou.csv")