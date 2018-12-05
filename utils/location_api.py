import math


class LocationAPI:
    
    def __init__(self):
        self.R = 6371.01 
        self.degToRad = math.pi / 180.0

    def bearing(self, latitude1, longitude1, latitude2, longitude2):
        phi1 = latitude1 * self.degToRad
        phi2 = latitude2 * self.degToRad
        lam1 = longitude1 * self.degToRad
        lam2 = longitude2 * self.degToRad

        bearing = math.atan2(math.sin(lam2 - lam1) * math.cos(phi2),
                             math.cos(phi1) * math.sin(phi2) - math.sin(phi1) * math.cos(phi2) * math.cos(lam2 - lam1)
                             ) * 180 / math.pi

        if bearing < 0:
            bearing = bearing + 360

        return bearing
        
    def distance(self, latitude1, longitude1, latitude2, longitude2):
        phi1 = latitude1 * self.degToRad
        phi2 = latitude2 * self.degToRad
        lam1 = longitude1 * self.degToRad
        lam2 = longitude2 * self.degToRad

        # in meter
        return self.R * math.acos(math.sin(phi1) * math.sin(phi2) + math.cos(phi1) * math.cos(phi2) * math.cos(lam2 - lam1)) * 1000

    def direction(self, bearing):
        # 0 Degree
        if (0.0 <= bearing < 15.0) or (345.0 <= bearing <= 360.0): return {'dx':-2, 'dy':0}
        # 30 Degree
        elif (15.0 <= bearing < 30.0) or (30.0 <= bearing < 37.5): return {'dx': -2, 'dy': +1}
        # 45 Degree
        elif (37.5 <= bearing < 45.0) or (45.0 <= bearing < 52.5): return {'dx': -2, 'dy': +2}
        # 60 Degree
        elif (52.5 <= bearing < 60.0) or (60.0 <= bearing < 75.0): return {'dx': -1, 'dy': +2}
        # 90 Degree
        elif (75.0 <= bearing < 90.0) or (90.0 <= bearing < 105.0): return {'dx': 0, 'dy': +2}
        # 120 Degree
        elif (105.0 <= bearing < 120.0) or (120.0 <= bearing < 127.5): return {'dx': +1, 'dy': +2}
        # 135 Degree
        elif (127.5 <= bearing < 135.0) or (135.0 <= bearing < 142.5): return {'dx': +2, 'dy': +2}
        # 150 Degree
        elif (142.5 <= bearing < 150.0) or (150.0 <= bearing < 165.0): return {'dx': +2, 'dy': +1}
        # 180 Degree
        elif (165.0 <= bearing < 180.0) or (180.0 <= bearing < 195.0): return {'dx': +2, 'dy': 0}
        # 210 Degree
        elif (195.0 <= bearing < 210.0) or (210.0 <= bearing < 217.5): return {'dx': +2, 'dy': -1}
        # 225 Degree
        elif (217.5 <= bearing < 225.0) or (225.0 <= bearing < 232.5): return {'dx': +2, 'dy': -2}
        # 240 Degree
        elif (232.5 <= bearing < 240.0) or (240.0 <= bearing < 255.0): return {'dx': +1, 'dy': -2}
        # 270 Degree
        elif (225.0 <= bearing < 270.0) or (270.0 <= bearing < 285.0): return {'dx': 0, 'dy': -2}
        # 300 Degree
        elif (285.0 <= bearing < 300.0) or (300.0 <= bearing < 307.5): return {'dx': -1, 'dy': -2}
        # 315 Degree
        elif (307.5 <= bearing < 315.0) or (315.0 <= bearing < 322.5): return {'dx': -2, 'dy': -2}
        # 330 Degree
        elif (322.5 <= bearing < 330.0) or (330.0 <= bearing < 345.5): return {'dx': -2, 'dy': -1}


if __name__ == '__main__':

    # ex) distance == 약 100m
    distance = LocationAPI().distance(latitude1=35.153056,
                                      longitude1=129.131650,
                                      latitude2=35.153054,
                                      longitude2=129.131872)
    print(distance)

    bearing = LocationAPI().bearing(latitude1=35.153056,
                                    longitude1=129.131650,
                                    latitude2=35.152961,
                                    longitude2=129.132747)
    print(bearing)

    bearing2 = LocationAPI().bearing(latitude1=-35.153052,
                                    longitude1=129.132744,
                                    latitude2=-35.152960,
                                    longitude2=129.132639)
    print(bearing2)

    locationAPI = LocationAPI()
    direction = locationAPI.direction(bearing=12.2)
    print(derection['dx'], direction['dy'])
