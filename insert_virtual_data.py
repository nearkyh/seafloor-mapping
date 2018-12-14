import pandas as pd
import csv
import time

from utils.db_connector import DBConnector
from utils.location_api import LocationAPI


db_conn = DBConnector()
conn = db_conn.connect_mysql()

data = 'virtual_data2.csv'
f = open('{0}'.format(data), 'r')
csvReader = csv.reader(f)

rowArr = []
for row in csvReader:
    rowArr.append(row)
f.close()

del rowArr[0]

dataQueue = []
dataQueue2 = []
for i in range(len(rowArr)):
    latitude = '{0:.6f}'.format(float(rowArr[i][0]))
    longitude = '{0:.6f}'.format(float(rowArr[i][1]))
    depth = float(rowArr[i][2])
    timestamp = 0

    print(latitude, longitude, depth)
    dataQueue.append(latitude)
    dataQueue2.append(longitude)

    if len(dataQueue) > 1:
        distance = LocationAPI().distance(latitude1=float(dataQueue[-2:][0]),
                                          longitude1=float(dataQueue2[-2:][0]),
                                          latitude2=float(dataQueue[-2:][1]),
                                          longitude2=float(dataQueue2[-2:][1]))
        print(distance)
        if 8.0 <= distance <= 12.0:
            print("ok")

    time.sleep(2)

    db_conn.insert_data2(
        conn=conn,
        latitude=latitude,
        longitude=longitude,
        depth=depth,
        timestamp=timestamp)
