import pandas as pd
import csv
import datetime
import sys

# ETA読み込み
args = sys.argv
file = "data/"+args[1]+"_etatable.csv"
f = pd.read_csv(file, header=None)

# 絞り込み
use = f[[0,1,2]]
# use[2] = pd.to_timedelta(use[2]) 
# use[2]は秒数での00:00:00からの経過時間が入っている
weekday_bin = use.groupby([0,1])

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
eva[9] = eva[9].dt.total_seconds() # 時間を秒単位に変換
consyu = eva.groupby([3,8])
consyu = consyu.mean()

youbi = 0
evaluation = list()
# aho = "tt"+args[1]
# str(aho)

while youbi <= 4:
    #曜日ごと
    binnmei = 0
    while binnmei <= 12:
        # 便ごと
        table = ttkeiiku[binnmei] #tableには秒数で絶対時刻が入ってる
        binnmei = binnmei + 1
        tmpbin = str(binnmei)
        target = "A"+tmpbin
        # consyuがプラマイ秒でweekday_binが秒の絶対時刻。そのためtableを＋してkekkaには差分だけ入れる
        print(consyu.loc[youbi, target])
        
        # kekka = consyu.loc[youbi, target] - weekday_bin.loc[youbi, target] + table # kekkaは秒数、時刻表からのプラマイで入ってる。小さほど正義
        # evaluation.append([youbi, target, kekka])
    youbi = youbi + 1
    

# # csvに書き込み
# with open('evaluation/'+args[1]+'_A.csv', 'w') as file:
#     writer = csv.writer(file, lineterminator='\n')
#     writer.writerows(evaluation)

