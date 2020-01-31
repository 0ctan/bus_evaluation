import pandas as pd
import csv
import datetime
import sys

# ETA読み込み
args = sys.argv
file = "data/"+args[1]+"_etatable.csv"
etadict = []

with open(file, newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)
        etadict.append(row)

# 今週のdata読み込み
file2 = "data/eva"+args[1]+".csv"
f2 = pd.read_csv(file2, header=None)
eva = f2[[3,8,9]]
eva[9] = pd.to_timedelta(eva[9])
eva[9] = eva[9].dt.total_seconds() # 時間を秒単位に変換
consyu = eva.groupby([3,8])




length = len(etadict)

print(etadict[0][2])
youbi = 0

while youbi <= 4:
    #曜日ごと
    binnmei = 0
    while binnmei <= 12:
        # 便ごと
        table = aho[binnmei] #tableには秒数で絶対時刻が入ってる
        binnmei = binnmei + 1
        tmpbin = str(binnmei)
        target = "A"+tmpbin
        # consyuがプラマイ秒でweekday_binが秒の絶対時刻。そのためtableを＋してkekkaには差分だけ入れる
        print(consyu.loc[youbi, target])
        # kekka = consyu.loc[youbi, target] - weekday_bin.loc[youbi, target] + table # kekkaは秒数、時刻表からのプラマイで入ってる。小さほど正義
        # evaluation.append([youbi, target, kekka])
    youbi = youbi + 1
    

# for n in range(length)