import pandas as pd
import csv
import datetime
import sys

# ETA読み込み
args = sys.argv
file = "data/"+args[1]+"_etatable.csv"
f = pd.read_csv(file, header=None)

# 絞り込み
use = f[[3,8,9]]
use[9] = pd.to_timedelta(use[9])
use[9] = use[9].dt.total_seconds()
weekday_bin = use.groupby([3,8])

# print(weekday_bin.groups)
# mean = weekday_bin.mean()
# csvに書き込み
# mean.to_csv("ave_delayall.csv")
# print(mean.loc[0,'A1']) # 月曜のA1便の平均遅延

# 今週の運行情報読み込み
file2 = "data/eva"+args[1]+".csv"
f2 = pd.read_csv(file2, header=None)
eva = f2[[3,8,9]]
eva[9] = pd.to_timedelta(eva[9])
eva[9] = eva[9].dt.total_seconds()
weekday_bin_eva = eva.groupby([3,8])

youbi = 0
evaluation = list()

while youbi <= 4:
    #曜日ごと
    binnmei = 0
    while binnmei <= 12:
        # 便ごと
        binnmei = binnmei + 1
        tmpbin = str(binnmei)
        target = "A"+tmpbin
        kekka = weekday_bin_eva.loc[youbi, target] - weekday_bin.loc[youbi, target] # kekkaは秒数、時刻表からのプラマイで入ってる。小さほど正義
        evaluation.append([youbi, target, kekka])
    youbi = youbi + 1
    

# csvに書き込み
with open('evaluation/'+args[1]+'_A.csv', 'w') as file:
    writer = csv.writer(file, lineterminator='\n')
    writer.writerows(evaluation)

