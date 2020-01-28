a = 0
h = [7,8,9,9,10,11,11,12,13,13,14,15,16]
m = [56,36,16]
h1= [8,9,9,10,11,11,12,13,14,14,15,16,16]
m1= [35,15,55]

th=[23,23,0,1,1,2,3,3,4,5,5,6,7]
tm=[6,46,26]
while a <=12:
    # m = (m+a*40)%60
    # m1 = (m1+a*40)%60
    # tm = (tm+a*40)%60
    lnum=a+1
    print('elif datetime.time('+str(h[a])+','+str(m[a%3])+')<= jstime <= datetime.time('+str(h1[a])+','+str(m1[a%3])+'):')
    print('    # A'+str(lnum)+'便に該当')
    print('    table = datetime.datetime(lyear[n], lmonth[n], lday[n],'+str(th[a])+','+str(tm[a%3])+')')
    print('    table = table + datetime.timedelta(hours=+9)')
    print('    delay = jst- table')
    print('    A'+str(lnum)+'.append([jst, delay])')
    a = lnum
