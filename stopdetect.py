import pandas as pd
import sys
import datetime

args = sys.argv

file = args[1]

filename = pd.read_csv(file)

# 配列に格納
lyear = []
lmonth = []
lday = []
lh = []
lmin = []
lsec = []
llat = []
llon = []

lyear= filename['year']
lmonth= filename['month']
lday = filename['day']
lh = filename['h']
lmin = filename['min']
lsec = filename['sec']
llat = filename['lat']
llon = filename['lon']

length = len(lyear)
timeout = 0

# 基準は+-0.0002以内かどうか


for n in range(length):
    if 23 <= h[n] or h[n]<8 : # 08:00:00〜16:59:59(JST)まで有効コードはUTC表記
        if 35.3076<listlat[n]<35.3080 : # 慶育病院
            if 139.4313<listlon[n]<139.4317 :
                # 慶育判定
                timeout =　
            
