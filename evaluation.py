import pandas as pd
import csv
import datetime
import sys

args = sys.argv
file = "data/"+args[1]+".csv"

print(file)

f = pd.read_csv(file, header=None)
# 絞り込み
use = f[[3,8,9]]
use[9] = pd.to_timedelta(use[9])
use[9] = use[9].dt.total_seconds()

weekday_bin = use.groupby([3,8])
# print(weekday_bin.groups)
mean = weekday_bin.mean()
# csvに書き込み
# mean.to_csv("ave_delayall.csv")


# print(mean.loc[0,'A1']) # 月曜のA1便の平均遅延

# 時刻表データ
tt = pd.read_csv("data/timetable.csv")
# 配列に入れる
ttbin = []
ttyokado = []
ttshonandai = []
ttkeiiku = []

ttbin = tt['bin']
ttyokado = tt['yokado']
ttshonandai = tt['shonandai']
ttkeiiku = tt['keiiku']

youbi = 0
etatable = list()

while youbi <= 4:
    #曜日ごと
    binnmei = 0
    while binnmei <= 12:
        # 便ごと
        table = ttyokado[binnmei]
        binnmei = binnmei + 1
        tmpbin = str(binnmei)
        target = "A"+tmpbin
        baka = mean.loc[youbi, target]
        baka = float(baka)
        eta = table + baka # ETAは秒数、時刻表からのプラマイで入ってる
        
        etatable.append([youbi, target, eta])


    youbi = youbi + 1
    

# # csvに書き込み
# with open('data/yokado_etatable.csv', 'w') as file:
#     writer = csv.writer(file, lineterminator='\n')
#     writer.writerows(etatable)

