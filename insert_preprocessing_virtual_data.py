import pandas as pd
import csv
import time

from utils.db_connector import DBConnector
from utils.location_api import LocationAPI


db_conn = DBConnector()
conn = db_conn.connect_mysql()
locationAPI = LocationAPI()

data = 'virtual_data.csv'
f = open('{0}'.format(data), 'r')
csvReader = csv.reader(f)

rowArr = []
for row in csvReader:
    rowArr.append(row)
f.close()

del rowArr[0]

latitudeQueue = []
longitudeQueue = []
depthQueue = []
for i in range(len(rowArr)):
    latitude = '{0:.6f}'.format(float(rowArr[i][0]))
    longitude = '{0:.6f}'.format(float(rowArr[i][1]))
    depth = float(rowArr[i][2])
    timestamp = 0

    latitudeQueue.append(latitude)
    longitudeQueue.append(longitude)
    depthQueue.append(depth)

    if len(latitudeQueue) > 1:
        locationAPI.data_preprocessing(latitude1=float(latitudeQueue[-2:][0]),
                                       longitude1=float(longitudeQueue[-2:][0]),
                                       depth1=float(depthQueue[-2:][0]),
                                       latitude2=float(latitudeQueue[-2:][1]),
                                       longitude2=float(longitudeQueue[-2:][1]),
                                       depth2=float(depthQueue[-2:][1]))

    time.sleep(1)

    if len(locationAPI.availableData) > 0:
        print(locationAPI.availableData[-1])
        print(locationAPI.availableData[-1]['latitude'], locationAPI.availableData[-1]['longitude'], locationAPI.availableData[-1]['depth'])

        # db_conn.insert_data2(
        #     conn=conn,
        #     latitude=latitude,
        #     longitude=longitude,
        #     depth=depth,
        #     timestamp=timestamp)

# for i in range(len(locationAPI.availableData)):
#     print(locationAPI.availableData[i])
# print(len(locationAPI.availableData))
# print(locationAPI.dataQueue)