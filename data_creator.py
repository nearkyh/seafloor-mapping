import csv
import math
import numpy as np
import random

def data_creator(initLatitude, initLongitude, latitudeLen, longitudeLen):
    rightRange = 1
    bottomRange = 1
    initRange = 0
    rLatitude = 0.0
    rLongitude = 0.0

    filePath = 'sample4.csv'
    with open(filePath, 'r') as f:
        csvReader = csv.reader(f)
        data = []
        for row in csvReader:
            data.append(row)

    # data = np.zeros([20, 20])
    # for i in range(20):
    #     for j in range(20):
    #         data[i, j] = random.uniform(1.0, 2.0)
    #
    # for i in range(16, 19):
    #     for j in range(16, 19):
    #         data[i, j] = random.uniform(8.0, 9.0)
    #
    # for i in range(2, 4):
    #     for j in range(0, 2):
    #         data[i, j] = random.uniform(5.0, 6.0)
    #
    # for i in range(7, 11):
    #     for j in range(2, 4):
    #         data[i, j] = random.uniform(4.0, 5.0)
    #
    # for i in range(10, 17):
    #     for j in range(10, 17):
    #         data[i, j] = random.uniform(3.0, 4.0)
    #
    # for i in range(12, 15):
    #     for j in range(0, 2):
    #         data[i, j] = random.uniform(5.0, 6.0)

    for y in range(longitudeLen):
        for x in range(latitudeLen):
            print(str(initLatitude) + ',' + str(initLongitude + initRange) + ',' +  str(data[y][x]))
            initRange += rightRange
            if x == 19:
                initRange = 0
        initLatitude += bottomRange


    return rLatitude, rLongitude

initLatitude = 100
initLongitude = 100
latitudeLen = 20
longitudeLen = 20
data_creator(initLatitude=initLatitude,
             initLongitude=initLongitude,
             latitudeLen=latitudeLen,
             longitudeLen=longitudeLen)
