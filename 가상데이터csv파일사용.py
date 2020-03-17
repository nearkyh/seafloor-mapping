def input_virtualData(self):
    data = 'virtual_data.csv'
    f = open('{0}'.format(data), 'r')
    csvReader = csv.reader(f)

    rowArr = []
    for row in csvReader:
        rowArr.append(row)
    f.close()

    # Remove label
    del rowArr[0]

    # First point(depth)
    dx, dy = 0, 0
    firstDepthValue = float(rowArr[1][2])

    # Surface plot data
    depth = self.axisZ - firstDepthValue
    z = np.array([[depth, 0.0], [0.0, 0.0]])
    # z = np.array([[depth, depth], [depth, depth]])
    colorMap = self.comboBox_colorMap.currentText()
    cmap = plt.get_cmap(colorMap)
    minZ = np.min(z)
    maxZ = np.max(z)
    rgba_img = cmap((z - minZ) / (maxZ - minZ))

    ## Add a grid to the view
    gls_item = gl.GLSurfacePlotItem(x=None, y=None, z=z, colors=rgba_img)
    gls_item.scale(x=1, y=1, z=1)
    gls_item.translate(dx=dx, dy=dy, dz=0)
    self.graphicsView.addItem(gls_item)
    self.depthQueue.append(z)

    queueSize = 2
    latitudeQueue = [] * queueSize
    longitudeQueue = [] * queueSize
    depthQueue = [] * queueSize
    dxQueue = [0]
    dyQueue = [0]
    smoothRange = 1
    for i in range(len(rowArr)):
        latitude = '{0:.6f}'.format(float(rowArr[i][0]))
        longitude = '{0:.6f}'.format(float(rowArr[i][1]))
        depth = float(rowArr[i][2])

        latitudeQueue.append(latitude)
        longitudeQueue.append(longitude)
        depthQueue.append(depth)

        if len(latitudeQueue[-queueSize:]) > 1:
            distance = locationAPI.distance(latitude1=float(latitudeQueue[-2:][0]),
                                            longitude1=float(longitudeQueue[-2:][0]),
                                            latitude2=float(latitudeQueue[-2:][1]),
                                            longitude2=float(longitudeQueue[-2:][1]))
            bearing = locationAPI.bearing(latitude1=float(latitudeQueue[-2:][0]),
                                          longitude1=float(longitudeQueue[-2:][0]),
                                          latitude2=float(latitudeQueue[-2:][1]),
                                          longitude2=float(longitudeQueue[-2:][1]))
            direction = locationAPI.direction2(bearing=bearing)
            dx =  dx + direction['dx']
            dy = dy + direction['dy']
            dxQueue.append(dx)
            dyQueue.append(dy)

            # Surface plot data
            depth = self.axisZ - depth
            z = np.array([[depth, 0.0], [0.0, 0.0]])
            colorMap = self.comboBox_colorMap.currentText()
            cmap = plt.get_cmap(colorMap)
            minZ = np.min(z)
            maxZ = np.max(z)
            rgba_img = cmap((z - minZ) / (maxZ - minZ))

            ## Add a grid to the view
            gls_item = gl.GLSurfacePlotItem(x=None, y=None, z=z, colors=rgba_img)
            gls_item.scale(x=1, y=1, z=1)
            gls_item.translate(dx=dx, dy=dy, dz=0)
            self.graphicsView.addItem(gls_item)
            self.depthQueue.append(z)

            # Smoothing graph, 현재 좌표에 대한 주변 8곳을 현재 좌표의 Depth 값으로 Mapping
            if (dx == dx) and (dy == dy):
                gls_item = gl.GLSurfacePlotItem(x=None, y=None, z=z, colors=rgba_img)
                gls_item.scale(x=1, y=1, z=1)
                gls_item.translate(dx=dx, dy=dy + smoothRange, dz=0)
                self.graphicsView.addItem(gls_item)
                self.depthQueue.append(z)
                gls_item = gl.GLSurfacePlotItem(x=None, y=None, z=z, colors=rgba_img)
                gls_item.scale(x=1, y=1, z=1)
                gls_item.translate(dx=dx + smoothRange, dy=dy, dz=0)
                self.graphicsView.addItem(gls_item)
                self.depthQueue.append(z)
                gls_item = gl.GLSurfacePlotItem(x=None, y=None, z=z, colors=rgba_img)
                gls_item.scale(x=1, y=1, z=1)
                gls_item.translate(dx=dx, dy=dy - smoothRange, dz=0)
                self.graphicsView.addItem(gls_item)
                self.depthQueue.append(z)
                gls_item = gl.GLSurfacePlotItem(x=None, y=None, z=z, colors=rgba_img)
                gls_item.scale(x=1, y=1, z=1)
                gls_item.translate(dx=dx - smoothRange, dy=dy, dz=0)
                self.graphicsView.addItem(gls_item)
                self.depthQueue.append(z)
                gls_item = gl.GLSurfacePlotItem(x=None, y=None, z=z, colors=rgba_img)
                gls_item.scale(x=1, y=1, z=1)
                gls_item.translate(dx=dx + smoothRange, dy=dy + smoothRange, dz=0)
                self.graphicsView.addItem(gls_item)
                self.depthQueue.append(z)
                gls_item = gl.GLSurfacePlotItem(x=None, y=None, z=z, colors=rgba_img)
                gls_item.scale(x=1, y=1, z=1)
                gls_item.translate(dx=dx - smoothRange, dy=dy - smoothRange, dz=0)
                self.graphicsView.addItem(gls_item)
                self.depthQueue.append(z)
                gls_item = gl.GLSurfacePlotItem(x=None, y=None, z=z, colors=rgba_img)
                gls_item.scale(x=1, y=1, z=1)
                gls_item.translate(dx=dx + smoothRange, dy=dy - smoothRange, dz=0)
                self.graphicsView.addItem(gls_item)
                self.depthQueue.append(z)
                gls_item = gl.GLSurfacePlotItem(x=None, y=None, z=z, colors=rgba_img)
                gls_item.scale(x=1, y=1, z=1)
                gls_item.translate(dx=dx - smoothRange, dy=dy + smoothRange, dz=0)
                self.graphicsView.addItem(gls_item)
                self.depthQueue.append(z)

# Scattering test
# plt.scatter(dxQueue, dyQueue, color='b', marker='o')
# plt.show()

def input_virtualData(self):
    self.reset_3D_surface()

    data = 'virtual_data.csv'
    f = open('{0}'.format(data), 'r')
    csvReader = csv.reader(f)

    rowArr = []
    for row in csvReader:
        rowArr.append(row)
    f.close()

    # Remove label
    del rowArr[0]

    # Data queue
    queueSize = 2
    latitudeQueue = [] * queueSize
    longitudeQueue = [] * queueSize
    depthQueue = [] * queueSize
    # First point(depth)
    dx, dy = 100, 100   # Center point
    dxQueue = [dx]
    dyQueue = [dy]
    for i in range(len(rowArr)):
        latitude = '{0:.6f}'.format(float(rowArr[i][0]))
        longitude = '{0:.6f}'.format(float(rowArr[i][1]))
        depth = float(rowArr[i][2])

        latitudeQueue.append(latitude)
        longitudeQueue.append(longitude)
        depthQueue.append(depth)

        if len(latitudeQueue[-queueSize:]) > 1:
            distance = locationAPI.distance(latitude1=float(latitudeQueue[-2:][0]),
                                            longitude1=float(longitudeQueue[-2:][0]),
                                            latitude2=float(latitudeQueue[-2:][1]),
                                            longitude2=float(longitudeQueue[-2:][1]))
            bearing = locationAPI.bearing(latitude1=float(latitudeQueue[-2:][0]),
                                          longitude1=float(longitudeQueue[-2:][0]),
                                          latitude2=float(latitudeQueue[-2:][1]),
                                          longitude2=float(longitudeQueue[-2:][1]))
            direction = locationAPI.direction5(bearing=bearing)
            dx =  dx + direction['dx']
            dy = dy + direction['dy']
            dxQueue.append(dx)
            dyQueue.append(dy)

    # 3D mapping with depth value
    if len(dxQueue) == len(dyQueue) == len(depthQueue):
        depthQueue2 = [self.axisZ - depthQueue[0]]
        for i in range(len(depthQueue)):
            '''
                The latitude and longitude below are normalized data
                that determines the direction on the 3D graph.
            '''
            latitude = dxQueue[i]
            longitude = dyQueue[i]
            depth = depthQueue[i]
            depth = self.axisZ - depth
            self.dataArr[latitude, longitude] = depth

            # Apply smoothing graph
            smoothRange = 4
            depthQueue2.append(depth)
            if (dxQueue[i] == latitude) and (dyQueue[i] == longitude):
                if len(depthQueue2) > 1:
                    # Mapping 될 지점의 Depth 값은 주변의 Depth 값들의 평균 값을 계산하여 적용
                    depth = float((depthQueue2[-2:][0] + depthQueue2[-2:][1]) / 2)
                    # Mapping 될 지점의 Depth 값은 주변의 Depth 값들 사이의 난수를 적용
                    # depth = random.uniform(depthQueue2[-2:][0], depthQueue2[-2:][1])
                    # print(depthQueue2[-2:][0], depthQueue2[-2:][1])
                    # 현재 좌표에 대한 주변 8곳을 현재 좌표의 Depth 값으로 Mapping
                    smoothingPoint = LocationAPI().smoothing_point(smoothRange=smoothRange)
                    for i in smoothingPoint:
                        x = i[0]
                        y = i[1]
                        self.dataArr[latitude + x, longitude + y] = depth

                    # for smoothRange in range(2):
                    #     # 0, 360 Degree (dx=-1, dy=0)
                    #     self.dataArr[latitude - smoothRange, longitude] = depth
                    #     # 45 Degree (dx=-1, dy=+1)
                    #     self.dataArr[latitude - smoothRange, longitude + smoothRange] = depth
                    #     # 90 Degree (dx=0, dy=+1)
                    #     self.dataArr[latitude, longitude + smoothRange] = depth
                    #     # 135 Degree (dx=+1, dy=+1)
                    #     self.dataArr[latitude + smoothRange, longitude + smoothRange] = depth
                    #     # 180 Degree (dx=+1, dy=0)
                    #     self.dataArr[latitude + smoothRange, longitude] = depth
                    #     # 225 Degree (dx=+1, dy=-1)
                    #     self.dataArr[latitude + smoothRange, longitude - smoothRange] = depth
                    #     # 270 Degree (dx=0, dy=-1)
                    #     self.dataArr[latitude, longitude - smoothRange] = depth
                    #     # 315 Degree (dx=-1, dy=-1)
                    #     self.dataArr[latitude - smoothRange, longitude - smoothRange] = depth

    # Surface plot data
    z = self.dataArr
    colorMap = self.comboBox_colorMap.currentText()
    cmap = plt.get_cmap(colorMap)
    minZ = np.min(z)
    maxZ = np.max(z)
    rgba_img = cmap((z - minZ) / (maxZ - minZ))

    # Add a grid to the view
    gls_item = gl.GLSurfacePlotItem(x=None, y=None, z=z, colors=rgba_img)
    gls_item.scale(x=1, y=1, z=1)
    gls_item.translate(dx=-100, dy=-100, dz=0)
    self.graphicsView.addItem(gls_item)
    self.depthQueue.append(z)


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

