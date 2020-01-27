import pandas as pd
import sys
import datetime
import csv

args = sys.argv

# file = args[1]
file = "data/clean.csv"

f = pd.read_csv(file)

# 配列に格納
lyear = []
lmonth = []
lday = []
lh = []
lmin = []
lsec = []
llat = []
llon = []

lyear= f['year']
lmonth= f['month']
lday = f['day']
lh = f['h']
lmin = f['min']
lsec = f['sec']
llat = f['lat']
llon = f['lon']

length = len(lyear)


# 基準は+-0.0002以内かどうか
busstopnow = list()

global keiikuflag
global yokadoflag
global shonanflag

for n in range(length):
    if 23 <= lh[n] or lh[n]<8 : # 08:00:00〜16:59:59(JST)まで有効コードはUTC表記
        if 35.3076<=llat[n]<=35.3080 : # 慶育病院
            if 139.4313<=llon[n]<=139.4317 :
                # 慶育判定
                time = datetime.datetime(lyear[n], lmonth[n], lday[n], lh[n], lmin[n], lsec[n])
                if keiikuflag < time:
                    # フラグなかったとき
                    busstopnow.append([lyear[n], lmonth[n], lday[n], lh[n], lmin[n], lsec[n], "keiiku"]) # リストに追加
                    keiikuflag = time + datetime.timedelta(minutes=25) # 25分後にフラグを設定
        if 35.3914<=llat[n]<=35.3918 : # よーかどー
            if 139.4471<=llon[n]<=139.4475 :
                # ヨーカどー判定
                time = datetime.datetime(lyear[n], lmonth[n], lday[n], lh[n], lmin[n], lsec[n])
                if yokadoflag < time:
                    # フラグなかったとき
                    busstopnow.append([lyear[n], lmonth[n], lday[n], lh[n], lmin[n], lsec[n], "yokado"]) # リストに追加
                    yokadoflag = time + datetime.timedelta(minutes=25)  # 25分後にフラグを設定
        if 35.3951<=llat[n]<=35.3955 : # 湘南台
            if 139.4662<=llon[n]<=139.4666 :
                # 湘南台判定
                time = datetime.datetime(lyear[n], lmonth[n], lday[n], lh[n], lmin[n], lsec[n])
                if shonanflag < time:
                    # フラグなかったとき
                    busstopnow.append([lyear[n], lmonth[n], lday[n], lh[n], lmin[n], lsec[n], "shonandai"]) # リストに追加
                    shonanflag = time + datetime.timedelta(minutes=25)  # 25分後にフラグを設定

# csvに書き込み
with open('data/stoptime.csv', 'w') as file:
    writer = csv.writer(file, lineterminator='\n')
    writer.writerows(busstopnow)
