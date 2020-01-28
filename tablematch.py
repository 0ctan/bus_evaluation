import pandas as pd
import datetime

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


for n in range(length):
    if lstop[n] == 'yokado':
        time = datetime.datetime(lyear[n], lmonth[n], lday[n], lh[n], lmin[n], lsec[n])
        jst = time + datetime.timedelta(hours=+9)
        jstime = jst.time()
        if datetime.time(7,56)<= jstime <= datetime.time(8,35):
            # A1便に該当
            table = datetime.datetime(lyear[n], lmonth[n], lday[n],23,6)
            table = table + datetime.timedelta(hours=+9)
            delay = jst- table
            print(delay)
            A1.append([jst, delay])
        elif datetime.time(8,36)<= jstime <= datetime.time(9,5):
            # A2便に該当
            table = datetime.datetime(lyear[n], lmonth[n], lday[n],23,46)
            table = table + datetime.timedelta(hours=+9)
            delay = jst- table
            A2.append([jst, delay])
        elif datetime.time(9,16)<= jstime <= datetime.time(9,45):
            # A3
            table = datetime.datetime(lyear[n], lmonth[n], lday[n],0,26)
            table = table + datetime.timedelta(hours=+9)
            delay = jst- table
            A3.append([jst, delay])
        elif datetime.time(9,56)<= jstime <= datetime.time(10,25):
            # A4
            table = datetime.datetime(lyear[n], lmonth[n], lday[n],1,6)
            table = table + datetime.timedelta(hours=+9)
            delay = jst- table
            A4.append([jst, delay])
        elif datetime.time(10,36)<= jstime <= datetime.time(11,5):
            # A5
            table = datetime.datetime(lyear[n], lmonth[n], lday[n],1,46)
            table = table + datetime.timedelta(hours=+9)
            delay = jst- table
            A5.append([jst, delay])
        elif datetime.time(9,56)<= jstime <= datetime.time(10,25):
            # A6
            table = datetime.datetime(lyear[n], lmonth[n], lday[n],23,6)
            table = table + datetime.timedelta(hours=+9)
            delay = jst- table
            A4.append([jst, delay])

