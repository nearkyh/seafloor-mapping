import csv

def data_creator(initLatitude, initLongitude, latitudeLen, longitudeLen):
    rightRange = 1
    bottomRange = 1
    initRange = 0
    rLatitude = 0.0
    rLongitude = 0.0

    filePath = 'test2.csv'
    with open(filePath, 'r') as f:
        csvReader = csv.reader(f)
        data = []
        for row in csvReader:
            data.append(row)

    for y in range(longitudeLen):
        for x in range(latitudeLen):
            print(str(initLatitude) + ',' + str(initLongitude + initRange) + ',' +  data[y][x])
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
