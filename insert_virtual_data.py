import pandas as pd
import csv

from utils.db_connector import DBConnector


db_conn = DBConnector()
conn = db_conn.connect_mysql()

data = 'virtual_data.csv'
f = open('{0}'.format(data), 'r')
csvReader = csv.reader(f)

rowArr = []
for row in csvReader:
    rowArr.append(row)
f.close()

del rowArr[0]

for i in range(len(rowArr)):
    latitude = '{0:.6f}'.format(float(rowArr[i][0]))
    longitude = '{0:.6f}'.format(float(rowArr[i][1]))
    depth = float(rowArr[i][2])
    timestamp = 0

    print(latitude, longitude, depth)

    # db_conn.insert_data(
    #     conn=conn,
    #     latitude=latitude,
    #     longitude=longitude,
    #     depth=depth,
    #     timestamp=timestamp)
