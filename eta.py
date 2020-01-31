import pandas as pd
import csv
import datetime

file = "data/weather.csv"

f = pd.read_csv(file, dtype={'date': datetime})


