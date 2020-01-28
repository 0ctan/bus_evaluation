# -*- coding: utf-8 -*-
import pandas as pd
import datetime
import csv

file = "data/stoptime.csv"

f = pd.read_csv(file)

# 配列に格納
lyear = []
lmonth = []
lday = []
lh = []
lmin = []
lsec = []
lstop = []

lyear= f['year']
lmonth= f['month']
lday = f['day']
lh = f['h']
lmin = f['min']
lsec = f['sec']
lstop = f['stop']

length = len(lyear)

A1 = []
A2 = []
A3 = []
A4 = []
A5 = []
A6 = []
A7 = []
A8 = []
A9 = []
A10 = []
A11 = []
A12 = []
A13 = []
csving = list()

for n in range(length):
    if lstop[n] == 'keiiku':
        time = datetime.datetime(lyear[n], lmonth[n], lday[n], lh[n], lmin[n], lsec[n])
        jst = time + datetime.timedelta(hours=+9)
        jstime = jst.time()
        if datetime.time(8,20)<= jstime <= datetime.time(8,59):
            # A1便に該当
            table = datetime.datetime(lyear[n], lmonth[n], lday[n],23,30)
            table = table + datetime.timedelta(hours=+9)
            delay = jst- table
            A1.append([jst, delay])
            csving.append([jst.year, jst.month, jst.day, jst.weekday(), jst.hour, jst.minute, jst.second, lstop[n], 'A1', delay])
        elif datetime.time(9,0)<= jstime <= datetime.time(9,39):
            # A2便に該当
            table = datetime.datetime(lyear[n], lmonth[n], lday[n],0,10)
            table = table + datetime.timedelta(hours=+9)
            delay = jst- table
            A2.append([jst, delay])
            csving.append([jst.year, jst.month, jst.day, jst.weekday(), jst.hour, jst.minute, jst.second, lstop[n], 'A2', delay])
        elif datetime.time(9,40)<= jstime <= datetime.time(10,19):
            # A3便に該当
            table = datetime.datetime(lyear[n], lmonth[n], lday[n],0,50)
            table = table + datetime.timedelta(hours=+9)
            delay = jst- table
            A3.append([jst, delay])
            csving.append([jst.year, jst.month, jst.day, jst.weekday(), jst.hour, jst.minute, jst.second, lstop[n], 'A3', delay])
        elif datetime.time(10,20)<= jstime <= datetime.time(10,59):
            # A4便に該当
            table = datetime.datetime(lyear[n], lmonth[n], lday[n],1,30)
            table = table + datetime.timedelta(hours=+9)
            delay = jst- table
            A4.append([jst, delay])
            csving.append([jst.year, jst.month, jst.day, jst.weekday(), jst.hour, jst.minute, jst.second, lstop[n], 'A4', delay])
        elif datetime.time(11,0)<= jstime <= datetime.time(11,39):
            # A5便に該当
            table = datetime.datetime(lyear[n], lmonth[n], lday[n],2,10)
            table = table + datetime.timedelta(hours=+9)
            delay = jst- table
            A5.append([jst, delay])
            csving.append([jst.year, jst.month, jst.day, jst.weekday(), jst.hour, jst.minute, jst.second, lstop[n], 'A5', delay])
        elif datetime.time(11,40)<= jstime <= datetime.time(12,19):
            # A6便に該当
            table = datetime.datetime(lyear[n], lmonth[n], lday[n],2,50)
            table = table + datetime.timedelta(hours=+9)
            delay = jst- table
            A6.append([jst, delay])
            csving.append([jst.year, jst.month, jst.day, jst.weekday(), jst.hour, jst.minute, jst.second, lstop[n], 'A6', delay])
        elif datetime.time(12,20)<= jstime <= datetime.time(12,59):
            # A7便に該当
            table = datetime.datetime(lyear[n], lmonth[n], lday[n],3,30)
            table = table + datetime.timedelta(hours=+9)
            delay = jst- table
            A7.append([jst, delay])
            csving.append([jst.year, jst.month, jst.day, jst.weekday(), jst.hour, jst.minute, jst.second, lstop[n], 'A7', delay])
        elif datetime.time(13,0)<= jstime <= datetime.time(13,39):
            # A8便に該当
            table = datetime.datetime(lyear[n], lmonth[n], lday[n],4,10)
            table = table + datetime.timedelta(hours=+9)
            delay = jst- table
            A8.append([jst, delay])
            csving.append([jst.year, jst.month, jst.day, jst.weekday(), jst.hour, jst.minute, jst.second, lstop[n], 'A8', delay])
        elif datetime.time(13,40)<= jstime <= datetime.time(14,19):
            # A9便に該当
            table = datetime.datetime(lyear[n], lmonth[n], lday[n],4,50)
            table = table + datetime.timedelta(hours=+9)
            delay = jst- table
            A9.append([jst, delay])
            csving.append([jst.year, jst.month, jst.day, jst.weekday(), jst.hour, jst.minute, jst.second, lstop[n], 'A9', delay])
        elif datetime.time(14,20)<= jstime <= datetime.time(14,59):
            # A10便に該当
            table = datetime.datetime(lyear[n], lmonth[n], lday[n],5,30)
            table = table + datetime.timedelta(hours=+9)
            delay = jst- table
            A10.append([jst, delay])
            csving.append([jst.year, jst.month, jst.day, jst.weekday(), jst.hour, jst.minute, jst.second, lstop[n], 'A10', delay])
        elif datetime.time(15,0)<= jstime <= datetime.time(15,39):
            # A11便に該当
            table = datetime.datetime(lyear[n], lmonth[n], lday[n],6,10)
            table = table + datetime.timedelta(hours=+9)
            delay = jst- table
            A11.append([jst, delay])
            csving.append([jst.year, jst.month, jst.day, jst.weekday(), jst.hour, jst.minute, jst.second, lstop[n], 'A11', delay])
        elif datetime.time(15,40)<= jstime <= datetime.time(16,19):
            # A12便に該当
            table = datetime.datetime(lyear[n], lmonth[n], lday[n],6,50)
            table = table + datetime.timedelta(hours=+9)
            delay = jst- table
            A12.append([jst, delay])
            csving.append([jst.year, jst.month, jst.day, jst.weekday(), jst.hour, jst.minute, jst.second, lstop[n], 'A12', delay])
        elif datetime.time(16,20)<= jstime <= datetime.time(16,59):
            # A13便に該当
            table = datetime.datetime(lyear[n], lmonth[n], lday[n],7,30)
            table = table + datetime.timedelta(hours=+9)
            delay = jst- table
            A13.append([jst, delay])
            csving.append([jst.year, jst.month, jst.day, jst.weekday(), jst.hour, jst.minute, jst.second, lstop[n], 'A13', delay])


# csvに書き込み
with open('data/keiiku.csv', 'w') as file:
    writer = csv.writer(file, lineterminator='\n')
    writer.writerows(csving)
