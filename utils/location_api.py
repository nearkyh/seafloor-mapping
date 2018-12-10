import math
import itertools


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

    def direction_creator(self, directionRange):
        degreeRange = float(45 / directionRange)
        degree360 = float(360)
        degree0 = float(0)
        degree45 = float(45)
        degree135 = float(135)
        degree225 = float(225)
        degree315 = float(315)

        # 315 Degree
        _x5 = -directionRange
        _y5 = -directionRange
        print('# {0} Degree'.format(degree315))
        for i in range(directionRange):
            print('elif ({0} <= bearing < {1}) or ({2} <= bearing < {3}):'.format(degree315 - degreeRange / 2, degree315, degree315, degree315 + degreeRange / 2), "return", {'dx': _x5, 'dy': _y5})
            degree315 += degreeRange
            _y5 += 1

        # 0, 360 Degree
        _x5 = -directionRange
        y0 = 0
        print('# {0}, {1} Degree'.format(degree0, degree360))
        for i in range(directionRange):
            print('elif ({0} <= bearing < {1}) or ({2} <= bearing < {3}):'.format(degree0 - degreeRange / 2, degree0, degree0, degree0 + degreeRange / 2), "return", {'dx': _x5, 'dy': y0})
            degree0 += degreeRange
            y0 += 1

        # 45 Degree
        _x5 = -directionRange
        y5 = directionRange
        print('# {0} Degree'.format(degree45))
        for j in range(2 * directionRange):
            print('elif ({0} <= bearing < {1}) or ({2} <= bearing < {3}):'.format(degree45 - degreeRange / 2, degree45, degree45, degree45 + degreeRange / 2), "return", {'dx': _x5, 'dy': y5})
            degree45 += degreeRange
            _x5 += 1

        # 135 Degree
        x5 = directionRange
        y5 = directionRange
        print('# {0} Degree'.format(degree135))
        for m in range(2 * directionRange):
            print('elif ({0} <= bearing < {1}) or ({2} <= bearing < {3}):'.format(degree135 - degreeRange / 2, degree135, degree135, degree135 + degreeRange / 2), "return", {'dx': x5, 'dy': y5})
            degree135 += degreeRange
            y5 -= 1

        # 225 Degree
        _y5 = -directionRange
        x5 = directionRange
        print('# {0} Degree'.format(degree225))
        for n in range(2 * directionRange):
            print('elif ({0} <= bearing < {1}) or ({2} <= bearing < {3}):'.format(degree225 - degreeRange / 2, degree225, degree225, degree225 + degreeRange / 2), "return", {'dx': x5, 'dy': _y5})
            degree225 += degreeRange
            x5 -= 1

    def direction1(selfs, bearing):
        # 315.0 Degree
        if (292.5 <= bearing < 315.0) or (315.0 <= bearing < 337.5): return {'dx': -1, 'dy': -1}
        # 0.0, 360.0 Degree
        elif (337.5 <= bearing < 0.0) or (0.0 <= bearing < 22.5): return {'dx': -1, 'dy': 0}
        # 45.0 Degree
        elif (22.5 <= bearing < 45.0) or (45.0 <= bearing < 67.5): return {'dx': -1, 'dy': 1}
        elif (67.5 <= bearing < 90.0) or (90.0 <= bearing < 112.5): return {'dx': 0, 'dy': 1}
        # 135.0 Degree
        elif (112.5 <= bearing < 135.0) or (135.0 <= bearing < 157.5): return {'dx': 1, 'dy': 1}
        elif (157.5 <= bearing < 180.0) or (180.0 <= bearing < 202.5): return {'dx': 1, 'dy': 0}
        # 225.0 Degree
        elif (202.5 <= bearing < 225.0) or (225.0 <= bearing < 247.5): return {'dx': 1, 'dy': -1}
        elif (247.5 <= bearing < 270.0) or (270.0 <= bearing < 292.5): return {'dx': 0, 'dy': -1}

    def direction2(self, bearing):
        # 315.0 Degree
        if (303.75 <= bearing < 315.0) or (315.0 <= bearing < 326.25): return {'dx': -2, 'dy': -2}
        elif (326.25 <= bearing < 337.5) or (337.5 <= bearing < 348.75): return {'dx': -2, 'dy': -1}
        # 0.0, 360.0 Degree
        elif (348.75 <= bearing < 0.0) or (0.0 <= bearing < 11.25): return {'dx': -2, 'dy': 0}
        elif (11.25 <= bearing < 22.5) or (22.5 <= bearing < 33.75): return {'dx': -2, 'dy': 1}
        # 45.0 Degree
        elif (33.75 <= bearing < 45.0) or (45.0 <= bearing < 56.25): return {'dx': -2, 'dy': 2}
        elif (56.25 <= bearing < 67.5) or (67.5 <= bearing < 78.75): return {'dx': -1, 'dy': 2}
        elif (78.75 <= bearing < 90.0) or (90.0 <= bearing < 101.25): return {'dx': 0, 'dy': 2}
        elif (101.25 <= bearing < 112.5) or (112.5 <= bearing < 123.75): return {'dx': 1, 'dy': 2}
        # 135.0 Degree
        elif (123.75 <= bearing < 135.0) or (135.0 <= bearing < 146.25): return {'dx': 2, 'dy': 2}
        elif (146.25 <= bearing < 157.5) or (157.5 <= bearing < 168.75): return {'dx': 2, 'dy': 1}
        elif (168.75 <= bearing < 180.0) or (180.0 <= bearing < 191.25): return {'dx': 2, 'dy': 0}
        elif (191.25 <= bearing < 202.5) or (202.5 <= bearing < 213.75): return {'dx': 2, 'dy': -1}
        # 225.0 Degree
        elif (213.75 <= bearing < 225.0) or (225.0 <= bearing < 236.25): return {'dx': 2, 'dy': -2}
        elif (236.25 <= bearing < 247.5) or (247.5 <= bearing < 258.75): return {'dx': 1, 'dy': -2}
        elif (258.75 <= bearing < 270.0) or (270.0 <= bearing < 281.25): return {'dx': 0, 'dy': -2}
        elif (281.25 <= bearing < 292.5) or (292.5 <= bearing < 303.75): return {'dx': -1, 'dy': -2}

    def direction3(self, bearing):
        # 315.0 Degree
        if (307.5 <= bearing < 315.0) or (315.0 <= bearing < 322.5): return {'dy': -3, 'dx': -3}
        elif (322.5 <= bearing < 330.0) or (330.0 <= bearing < 337.5): return {'dy': -2, 'dx': -3}
        elif (337.5 <= bearing < 345.0) or (345.0 <= bearing < 352.5): return {'dy': -1, 'dx': -3}
        # 0.0, 360.0 Degree
        elif (352.5 <= bearing < 0.0) or (0.0 <= bearing < 7.5): return {'dy': 0, 'dx': -3}
        elif (7.5 <= bearing < 15.0) or (15.0 <= bearing < 22.5): return {'dy': 1, 'dx': -3}
        elif (22.5 <= bearing < 30.0) or (30.0 <= bearing < 37.5): return {'dy': 2, 'dx': -3}
        # 45.0 Degree
        elif (37.5 <= bearing < 45.0) or (45.0 <= bearing < 52.5): return {'dy': 3, 'dx': -3}
        elif (52.5 <= bearing < 60.0) or (60.0 <= bearing < 67.5): return {'dy': 3, 'dx': -2}
        elif (67.5 <= bearing < 75.0) or (75.0 <= bearing < 82.5): return {'dy': 3, 'dx': -1}
        elif (82.5 <= bearing < 90.0) or (90.0 <= bearing < 97.5): return {'dy': 3, 'dx': 0}
        elif (97.5 <= bearing < 105.0) or (105.0 <= bearing < 112.5): return {'dy': 3, 'dx': 1}
        elif (112.5 <= bearing < 120.0) or (120.0 <= bearing < 127.5): return {'dy': 3, 'dx': 2}
        # 135.0 Degree
        elif (127.5 <= bearing < 135.0) or (135.0 <= bearing < 142.5): return {'dy': 3, 'dx': 3}
        elif (142.5 <= bearing < 150.0) or (150.0 <= bearing < 157.5): return {'dy': 2, 'dx': 3}
        elif (157.5 <= bearing < 165.0) or (165.0 <= bearing < 172.5): return {'dy': 1, 'dx': 3}
        elif (172.5 <= bearing < 180.0) or (180.0 <= bearing < 187.5): return {'dy': 0, 'dx': 3}
        elif (187.5 <= bearing < 195.0) or (195.0 <= bearing < 202.5): return {'dy': -1, 'dx': 3}
        elif (202.5 <= bearing < 210.0) or (210.0 <= bearing < 217.5): return {'dy': -2, 'dx': 3}
        # 225.0 Degree
        elif (217.5 <= bearing < 225.0) or (225.0 <= bearing < 232.5): return {'dy': -3, 'dx': 3}
        elif (232.5 <= bearing < 240.0) or (240.0 <= bearing < 247.5): return {'dy': -3, 'dx': 2}
        elif (247.5 <= bearing < 255.0) or (255.0 <= bearing < 262.5): return {'dy': -3, 'dx': 1}
        elif (262.5 <= bearing < 270.0) or (270.0 <= bearing < 277.5): return {'dy': -3, 'dx': 0}
        elif (277.5 <= bearing < 285.0) or (285.0 <= bearing < 292.5): return {'dy': -3, 'dx': -1}
        elif (292.5 <= bearing < 300.0) or (300.0 <= bearing < 307.5): return {'dy': -3, 'dx': -2}

    def direction5(self, bearing):
        # 315.0 Degree
        if (310.5 <= bearing < 315.0) or (315.0 <= bearing < 319.5): return {'dy': -5, 'dx': -5}
        elif (319.5 <= bearing < 324.0) or (324.0 <= bearing < 328.5): return {'dy': -4, 'dx': -5}
        elif (328.5 <= bearing < 333.0) or (333.0 <= bearing < 337.5): return {'dy': -3, 'dx': -5}
        elif (337.5 <= bearing < 342.0) or (342.0 <= bearing < 346.5): return {'dy': -2, 'dx': -5}
        elif (346.5 <= bearing < 351.0) or (351.0 <= bearing < 355.5): return {'dy': -1, 'dx': -5}
        # 0.0, 360.0 Degree
        elif (355.5 <= bearing < 0.0) or (0.0 <= bearing < 4.5): return {'dy': 0, 'dx': -5}
        elif (4.5 <= bearing < 9.0) or (9.0 <= bearing < 13.5): return {'dy': 1, 'dx': -5}
        elif (13.5 <= bearing < 18.0) or (18.0 <= bearing < 22.5): return {'dy': 2, 'dx': -5}
        elif (22.5 <= bearing < 27.0) or (27.0 <= bearing < 31.5): return {'dy': 3, 'dx': -5}
        elif (31.5 <= bearing < 36.0) or (36.0 <= bearing < 40.5): return {'dy': 4, 'dx': -5}
        # 45.0 Degree
        elif (40.5 <= bearing < 45.0) or (45.0 <= bearing < 49.5): return {'dy': 5, 'dx': -5}
        elif (49.5 <= bearing < 54.0) or (54.0 <= bearing < 58.5): return {'dy': 5, 'dx': -4}
        elif (58.5 <= bearing < 63.0) or (63.0 <= bearing < 67.5): return {'dy': 5, 'dx': -3}
        elif (67.5 <= bearing < 72.0) or (72.0 <= bearing < 76.5): return {'dy': 5, 'dx': -2}
        elif (76.5 <= bearing < 81.0) or (81.0 <= bearing < 85.5): return {'dy': 5, 'dx': -1}
        elif (85.5 <= bearing < 90.0) or (90.0 <= bearing < 94.5): return {'dy': 5, 'dx': 0}
        elif (94.5 <= bearing < 99.0) or (99.0 <= bearing < 103.5): return {'dy': 5, 'dx': 1}
        elif (103.5 <= bearing < 108.0) or (108.0 <= bearing < 112.5): return {'dy': 5, 'dx': 2}
        elif (112.5 <= bearing < 117.0) or (117.0 <= bearing < 121.5): return {'dy': 5, 'dx': 3}
        elif (121.5 <= bearing < 126.0) or (126.0 <= bearing < 130.5): return {'dy': 5, 'dx': 4}
        # 135.0 Degree
        elif (130.5 <= bearing < 135.0) or (135.0 <= bearing < 139.5): return {'dy': 5, 'dx': 5}
        elif (139.5 <= bearing < 144.0) or (144.0 <= bearing < 148.5): return {'dy': 4, 'dx': 5}
        elif (148.5 <= bearing < 153.0) or (153.0 <= bearing < 157.5): return {'dy': 3, 'dx': 5}
        elif (157.5 <= bearing < 162.0) or (162.0 <= bearing < 166.5): return {'dy': 2, 'dx': 5}
        elif (166.5 <= bearing < 171.0) or (171.0 <= bearing < 175.5): return {'dy': 1, 'dx': 5}
        elif (175.5 <= bearing < 180.0) or (180.0 <= bearing < 184.5): return {'dy': 0, 'dx': 5}
        elif (184.5 <= bearing < 189.0) or (189.0 <= bearing < 193.5): return {'dy': -1, 'dx': 5}
        elif (193.5 <= bearing < 198.0) or (198.0 <= bearing < 202.5): return {'dy': -2, 'dx': 5}
        elif (202.5 <= bearing < 207.0) or (207.0 <= bearing < 211.5): return {'dy': -3, 'dx': 5}
        elif (211.5 <= bearing < 216.0) or (216.0 <= bearing < 220.5): return {'dy': -4, 'dx': 5}
        # 225.0 Degree
        elif (220.5 <= bearing < 225.0) or (225.0 <= bearing < 229.5): return {'dy': -5, 'dx': 5}
        elif (229.5 <= bearing < 234.0) or (234.0 <= bearing < 238.5): return {'dy': -5, 'dx': 4}
        elif (238.5 <= bearing < 243.0) or (243.0 <= bearing < 247.5): return {'dy': -5, 'dx': 3}
        elif (247.5 <= bearing < 252.0) or (252.0 <= bearing < 256.5): return {'dy': -5, 'dx': 2}
        elif (256.5 <= bearing < 261.0) or (261.0 <= bearing < 265.5): return {'dy': -5, 'dx': 1}
        elif (265.5 <= bearing < 270.0) or (270.0 <= bearing < 274.5): return {'dy': -5, 'dx': 0}
        elif (274.5 <= bearing < 279.0) or (279.0 <= bearing < 283.5): return {'dy': -5, 'dx': -1}
        elif (283.5 <= bearing < 288.0) or (288.0 <= bearing < 292.5): return {'dy': -5, 'dx': -2}
        elif (292.5 <= bearing < 297.0) or (297.0 <= bearing < 301.5): return {'dy': -5, 'dx': -3}
        elif (301.5 <= bearing < 306.0) or (306.0 <= bearing < 310.5): return {'dy': -5, 'dx': -4}

    def smoothing_point(self, smoothRange):
        smoothRangeList = []
        if smoothRange:
            for i in range(-smoothRange, smoothRange + 1):
                smoothRangeList.append(i)
        '''
        if smoothRange == 1:
            for i in range(-1, 2): smoothRangeList.append(i)
        elif smoothRange == 2:
            for i in range(-2, 3): smoothRangeList.append(i)
        elif smoothRange == 3:
            for i in range(-3, 4): smoothRangeList.append(i)
        elif smoothRange == 4:
            for i in range(-4, 5): smoothRangeList.append(i)
        '''

        # Combinations with replacement
        list_cwr = list(itertools.combinations_with_replacement(smoothRangeList, 2))
        # Permutations
        list_p = list(itertools.permutations(smoothRangeList, 2))
        sum_list = list_cwr + list_p
        # Remove duplicate elements
        duplicate_list = list(set(sum_list))
        # Remove center point(0, 0)
        duplicate_list.remove((0, 0))

        return duplicate_list



if __name__ == '__main__':

    # ex) distance == 약 100m
    distance = LocationAPI().distance(latitude1=35.153056,
                                      longitude1=129.131650,
                                      latitude2=35.153054,
                                      longitude2=129.131872)

    bearing = LocationAPI().bearing(latitude1=35.153056,
                                    longitude1=129.131650,
                                    latitude2=35.152961,
                                    longitude2=129.132747)

    bearing2 = LocationAPI().bearing(latitude1=-35.153052,
                                    longitude1=129.132744,
                                    latitude2=-35.152960,
                                    longitude2=129.132639)

    locationAPI = LocationAPI()
    direction = locationAPI.direction2(bearing=12.2)
    # print(direction['dx'], direction['dy'])

    direction_creator = locationAPI.direction_creator
    direction_creator(directionRange=1)
