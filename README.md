# bus_evaluation
卒論評価取り

UTC JST変換はあとで
timetable.csvは00:00:00基準の秒数

## usage 

$python killnull.py data/hoge.csv
$python stopdetect.py
$python tablematch.py


weekdayと曜日の対応
    0: 月, 1: 火, 2: 水, 3: 木, 4: 金, 5: 土, 6: 日

## データの取得
mongoexport -d bus_location -c keiiku_A --out 20200102.csv --type csv --fields "time,lat,lon"

以上。はい簡単

mongoexport -d bus_location -c keiiku_A --out eve20200131.csv --type csv --fields "time,lat,lon"

## 有効ログ
書き日時以降
2019-12-09T08:45:02

