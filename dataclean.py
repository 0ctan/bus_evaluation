import pandas as pd
import sys

args = sys.argv

file = args[1]

filename = pd.read_csv(file)

# 配列に格納
listTime = []
listlat = []
listlon = []

listTime = filename['time']
listlat = filename['lat']
listlon = filename['lon']

length = len(listTime)
timeout = 0

# 基準は+-0.0002以内かどうか

for n in range(length):
    if 35.3076<listlat[n]<35.3080 : # 慶育病院
        if 139.4313<listlon[n]<139.4317 :
            # 慶育判定
            timeout =
        
