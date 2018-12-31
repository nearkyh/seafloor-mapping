# -*- coding: utf-8 -*-

'''
    Form implementation generated from reading ui file 'main.ui'
    python -m PyQt5.uic.pyuic -x main.ui -o ui.py
    Created by: PyQt5 UI code generator 5.11.3
    WARNING! All changes made in this file will be lost!

    Edit the ui.py :
        1. self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        --> import pyqtgraph.opengl as gl
            self.graphicsView = gl.GLViewWidget(self.centralwidget)

        2. MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        --> MainWindow.setWindowTitle(_translate("MainWindow", "3D Seafloor"))

        3. self.colorBar = QtWidgets.QGraphicsView(self.centralwidget)
        --> import pyqtgraph as pg
            self.colorBar = pg.GraphicsView(self.centralwidget)
'''

import sys
import numpy as np
np.seterr(divide='ignore', invalid='ignore')
import pandas as pd
import csv
import random

import pyqtgraph as pg
import pyqtgraph.opengl as gl
import matplotlib.pyplot as plt

from PyQt5 import QtCore, QtGui, QtWidgets
from pyqtgraph.Qt import QtCore, QtGui

# from utils.ui import Ui_MainWindow
from utils.ui_test import Ui_MainWindow
from utils.db_connector import DBConnector
from utils.location_api import LocationAPI
from utils.smoothing_graph import SmoothingGraph
from utils.color_bar import ColorBar


class MainForm(Ui_MainWindow):

    def __init__(self):
        super(MainForm, self).__init__()

        self.axisX = 200
        self.axisY = 200
        self.axisZ = 100.0
        self.dataArr = np.zeros([self.axisX, self.axisY])
        self.depthQueue = []

        self.initScale = {'x': int(self.axisX / 20), 'y': int(self.axisY / 20), 'z': 10}
        self.mapScale = {'x': 1, 'y': 1, 'z': 2}
        self.mapTranslate = {'dx': -int(self.axisX / 2), 'dy': -int(self.axisY / 2), 'dz': 0}
        self.cameraPosition = self.axisX * 3 / 2

        self.colorMap = 'viridis'
        self.colorMaps = {
            'Perceptually Uniform Sequential': [
                'viridis', 'plasma', 'inferno', 'magma'],
            'Sequential': [
                'Greys', 'Purples', 'Blues', 'Greens', 'Oranges', 'Reds',
                'YlOrBr', 'YlOrRd', 'OrRd', 'PuRd', 'RdPu', 'BuPu',
                'GnBu', 'PuBu', 'YlGnBu', 'PuBuGn', 'BuGn', 'YlGn'],
            'Sequential (2)': [
                'binary', 'gist_yarg', 'gist_gray', 'gray', 'bone', 'pink',
                'spring', 'summer', 'autumn', 'winter', 'cool', 'Wistia',
                'hot', 'afmhot', 'gist_heat', 'copper'],
            'Diverging': [
                'PiYG', 'PRGn', 'BrBG', 'PuOr', 'RdGy', 'RdBu',
                'RdYlBu', 'RdYlGn', 'Spectral', 'coolwarm', 'bwr', 'seismic'],
            'Qualitative': [
                'Pastel1', 'Pastel2', 'Paired', 'Accent',
                'Dark2', 'Set1', 'Set2', 'Set3',
                'tab10', 'tab20', 'tab20b', 'tab20c'],
            'Miscellaneous': [
                'flag', 'prism', 'ocean', 'gist_earth', 'terrain', 'gist_stern',
                'gnuplot', 'gnuplot2', 'CMRmap', 'cubehelix', 'brg', 'hsv',
                'gist_rainbow', 'rainbow', 'jet', 'nipy_spectral', 'gist_ncar']
        }
        
        self.set_timer()

    def connection_events(self):
        self.pushButton_push.clicked.connect(self.update_customData)
        self.pushButton_reset.clicked.connect(self.reset_data)
        self.comboBox_colorMap.currentIndexChanged['QString'].connect(self.update_colorMap)
        self.pushButton_connectDB.clicked.connect(self.connect_db)
        self.pushButton_updateDB.clicked.connect(self.update_db)
        self.pushButton_disconnectDB.clicked.connect(self.disconnect_db)
        self.pushButton_filePath.clicked.connect(self.open_filePath)

    def colorMapUi(self):
        self.comboBox_colorMap.addItems(self.colorMaps['Perceptually Uniform Sequential'])
        self.comboBox_colorMap.insertSeparator(len(self.colorMaps['Perceptually Uniform Sequential']))
        self.comboBox_colorMap.addItems(self.colorMaps['Sequential'])
        self.comboBox_colorMap.insertSeparator(len(self.colorMaps['Perceptually Uniform Sequential']) + 1
                                               + len(self.colorMaps['Sequential']))
        self.comboBox_colorMap.addItems(self.colorMaps['Sequential (2)'])
        self.comboBox_colorMap.insertSeparator(len(self.colorMaps['Perceptually Uniform Sequential']) + 1
                                               + len(self.colorMaps['Sequential']) + 1
                                               + len(self.colorMaps['Sequential (2)']))
        self.comboBox_colorMap.addItems(self.colorMaps['Diverging'])
        self.comboBox_colorMap.insertSeparator(len(self.colorMaps['Perceptually Uniform Sequential']) + 1
                                               + len(self.colorMaps['Sequential']) + 1
                                               + len(self.colorMaps['Sequential (2)']) + 1
                                               + len(self.colorMaps['Diverging']))
        self.comboBox_colorMap.addItems(self.colorMaps['Qualitative'])
        self.comboBox_colorMap.insertSeparator(len(self.colorMaps['Perceptually Uniform Sequential']) + 1
                                               + len(self.colorMaps['Sequential']) + 1
                                               + len(self.colorMaps['Sequential (2)']) + 1
                                               + len(self.colorMaps['Diverging']) + 1
                                               + len(self.colorMaps['Qualitative']))
        self.comboBox_colorMap.addItems(self.colorMaps['Miscellaneous'])

        # init colorMap, 'jet'
        self.comboBox_colorMap.setCurrentIndex(len(self.colorMaps['Perceptually Uniform Sequential']) +
                                               len(self.colorMaps['Sequential']) +
                                               len(self.colorMaps['Sequential (2)']) +
                                               len(self.colorMaps['Diverging']) +
                                               len(self.colorMaps['Qualitative']) +
                                               14 + 5)

    def view_colorBar(self):
        try:
            '''
            0.0 -> black
            0.2 -> red
            0.6 -> yellow
            1.0 -> white
            '''
            stops = np.r_[-1.0, -0.5, 0.5, 1.0]
            colors = np.array([[0, 0, 1, 0.7], [0, 1, 0, 0.2], [0, 0, 0, 0.8], [1, 0, 0, 1.0]])
            cm = pg.ColorMap(stops, colors)
            cb = ColorBar(cm, 20, 200, label='Depth')
            self.colorBar.scene().addItem(cb)
            cb.translate(55, 15)

        except Exception as e:
            print("[error code] view_colorBar\n", e)
            pass

    def update_customData(self):
        try:
            del self.graphicsView.items[2:]
            self.init_3D_surface()
            self.custom_3D_surface()

        except Exception as e:
            print("[error code] update_customData\n", e)
            pass

    def reset_data(self):
        try:
            self.reset_3D_surface()

        except Exception as e:
            print("[error code] reset_data\n", e)
            pass

    def update_colorMap(self):
        try:
            del self.graphicsView.items[2:]
            self.init_3D_surface()

            colorMap = self.comboBox_colorMap.currentText()
            cmap = plt.get_cmap(colorMap)
            for z in self.depthQueue:
                minZ = np.min(z)
                maxZ = np.max(z)
                rgba_img = cmap((z - minZ) / (maxZ - minZ))
                gls_item = gl.GLSurfacePlotItem(x=None,
                                                y=None,
                                                z=z,
                                                colors=rgba_img)
                gls_item.scale(x=self.mapScale['x'],
                               y=self.mapScale['y'],
                               z=self.mapScale['z'])
                gls_item.translate(dx=self.mapTranslate['dx'],
                                   dy=self.mapTranslate['dy'],
                                   dz=self.mapTranslate['dz'])
                self.graphicsView.addItem(gls_item)

        except Exception as e:
            print("[error code] update_colorMap\n", e)
            pass

    def init_3D_surface(self):
        try:
            # Set graphics view
            self.graphicsView.show()
            self.graphicsView.setBackgroundColor('k')
            self.graphicsView.setCameraPosition(distance=self.cameraPosition, elevation=None, azimuth=None)

            # Add a grid to the view
            glg = gl.GLGridItem()
            glg.scale(x=self.initScale['x'],
                      y=self.initScale['y'],
                      z=self.initScale['z'])
            glg.setDepthValue(10) # draw grid after surfaces since they may be translucent
            self.graphicsView.addItem(glg)

            # Simple surface plot example
            z = np.array([[0]])
            colorMap = self.comboBox_colorMap.currentText()
            cmap = plt.get_cmap(self.colorMap)
            minZ = np.min(z)
            maxZ = np.max(z)
            rgba_img = cmap((z - minZ) / (maxZ - minZ))

            # plt.imshow(z, cmap=cmap)
            # plt.colorbar()
            # plt.clim(minZ, maxZ)
            # plt.show()

            # gls_item = gl.GLSurfacePlotItem(x=None, y=None, z=z, smooth=True, shader='normalColor', glOptions='opaque')
            # gls_item = gl.GLSurfacePlotItem(x=x, y=y, z=z, colors=rgba_img)
            # gls_item = gl.GLSurfacePlotItem(x=None, y=None, z=z, shader='normalColor', color=(0.5, 0.5, 1, 1))
            gls_item = gl.GLSurfacePlotItem(x=None,
                                            y=None,
                                            z=z,
                                            colors=rgba_img)
            gls_item.scale(x=self.mapScale['x'],
                           y=self.mapScale['y'],
                           z=self.mapScale['z'])
            gls_item.translate(dx=self.mapTranslate['dx'],
                               dy=self.mapTranslate['dy'],
                               dz=self.mapTranslate['dz'])
            self.graphicsView.addItem(gls_item)
            self.depthQueue.append(z)

        except Exception as e:
            print("[error code] init_3D_surface\n", e)
            pass

    def custom_3D_surface(self):
        try:
            # Input custom data
            latitude = self.textEdit_latitude.toPlainText()
            latitude = int(latitude)
            longitude = self.textEdit_longitude.toPlainText()
            longitude = int(longitude)
            depth = self.textEdit_depth.toPlainText()
            depth = float(depth)
            depth = self.axisZ - depth

            # Surface plot data
            self.dataArr[latitude, longitude] = depth
            z = self.dataArr
            colorMap = self.comboBox_colorMap.currentText()
            cmap = plt.get_cmap(colorMap)
            minZ = np.min(z)
            maxZ = np.max(z)
            rgba_img = cmap((z - minZ) / (maxZ - minZ))

            # Add a grid to the view
            gls_item = gl.GLSurfacePlotItem(x=None,
                                            y=None,
                                            z=z,
                                            colors=rgba_img)
            gls_item.scale(x=self.mapScale['x'],
                           y=self.mapScale['y'],
                           z=self.mapScale['z'])
            gls_item.translate(dx=self.mapTranslate['dx'],
                               dy=self.mapTranslate['dy'],
                               dz=self.mapTranslate['dz'])
            self.graphicsView.addItem(gls_item)
            self.depthQueue.append(z)

            # Reset textEdit
            # if str(latitude):
            #     self.textEdit_latitude.setText("")
            # if str(longitude):
            #     self.textEdit_longitude.setText("")
            if str(depth):
                self.textEdit_depth.setText("")

        except Exception as e:
            print("[error code] custom_3D_surface\n", e)
            pass

    def reset_3D_surface(self):
        try:
            del self.graphicsView.items[2:]                     # Remove all graphics items
            del self.depthQueue[:]                              # Remove all depth
            self.dataArr = np.zeros([self.axisX, self.axisY])   # Remove all data array (depth)
            self.init_3D_surface()                              # Initialize graph
            self.textEdit_latitude.setText("")
            self.textEdit_longitude.setText("")
            self.textEdit_depth.setText("")

        except Exception as e:
            print("[error code] reset_3D_surface\n", e)

    def connect_db(self):
        try:
            self.real_time_graph()

        except Exception as e:
            print("[error code] connect_db\n", e)
            pass

    def disconnect_db(self):
        try:
            print("[Message] End timer thread, Disconnect DB")

        except Exception as e:
            print("[error code] disconnect_db\n", e)
            pass

        finally:
            self.end_timer()
            mysql_connector.close_mysql()

    def update_db(self):
        try:
            # Update DB
            self.reset_3D_surface()
            conn = mysql_connector.connect_mysql()
            data = mysql_connector.select_data(conn=conn)
            mysql_connector.close_mysql()
            firstLatitudeValue = float('{0:.6f}'.format(float(data[0][1])))
            firstLongitudeValue = float('{0:.6f}'.format(float(data[0][2])))
            firstDepthValue = float('{0:.6f}'.format(float(data[0][3])))

            # Data queue
            queueSize = 2
            latitudeQueue = [] * queueSize
            longitudeQueue = [] * queueSize
            depthQueue = [] * queueSize
            # First point(depth)
            dx, dy = int(self.axisX / 2), int(self.axisY / 2)   # Center point
            dxQueue = [dx]
            dyQueue = [dy]
            for i in range(len(data)):
                '''
                latitude  : data[i][1]
                longitude : data[i][2]
                depth     : data[i][3]
                '''
                latitude = float('{0:.6f}'.format(float(data[i][1])))
                longitude = float('{0:.6f}'.format(float(data[i][2])))
                depth = float('{0:.6f}'.format(float(data[i][3])))

                latitudeQueue.append(latitude)
                longitudeQueue.append(longitude)
                depthQueue.append(depth)

                if len(latitudeQueue[-queueSize:]) > 1:
                    distance = locationAPI.distance(latitude1=latitudeQueue[-2:][0],
                                                    longitude1=longitudeQueue[-2:][0],
                                                    latitude2=latitudeQueue[-2:][1],
                                                    longitude2=longitudeQueue[-2:][1])
                    bearing = locationAPI.bearing(latitude1=latitudeQueue[-2:][0],
                                                  longitude1=longitudeQueue[-2:][0],
                                                  latitude2=latitudeQueue[-2:][1],
                                                  longitude2=longitudeQueue[-2:][1])
                    direction = locationAPI.direction2(bearing=bearing)
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
                    '''
                    if locationAPI.direction1: smoothRange = 0
                    elif locationAPI.direction2: smoothRange = 1
                    elif locationAPI.direction3: smoothRange = 1
                    elif locationAPI.direction5: smoothRange = 2
                    '''
                    smoothRange = 1
                    if smoothRange > 0:
                        depthQueue2.append(depth)
                        if (dxQueue[i] == latitude) and (dyQueue[i] == longitude):
                            if len(depthQueue2) > 1:
                                # Mapping 될 지점의 Depth 값은 주변의 Depth 값들의 평균 값을 계산하여 적용
                                # depth = float((depthQueue2[-2:][0] + depthQueue2[-2:][1]) / 2)
                                # Mapping 될 지점의 Depth 값은 주변의 Depth 값들 사이의 float 형 난수를 적용
                                depth = random.uniform(float(depthQueue2[-2:][0]), float(depthQueue2[-2:][1]))

                                # 현재 좌표에 대한 주변 8곳을 현재 좌표의 Depth 값으로 Mapping
                                smoothingPoint = SmoothingGraph().smoothing_point(smoothRange=smoothRange)
                                for i in smoothingPoint:
                                    x = i[0]
                                    y = i[1]
                                    self.dataArr[latitude + x, longitude + y] = depth

                                # pst = SmoothingGraph().partial_smoothing_point(smoothRange=smoothRange)
                                # for pst_num in range(len(pst)):
                                #     for i in pst[pst_num]:
                                #         x = i[0]
                                #         y = i[1]
                                #         self.dataArr[latitude + x, longitude + y] = depth - (pst_num + 1)
                    else:
                        pass

            # Surface plot data
            z = self.dataArr
            colorMap = self.comboBox_colorMap.currentText()
            cmap = plt.get_cmap(colorMap)
            minZ = np.min(z)
            maxZ = np.max(z)
            rgba_img = cmap((z - minZ) / (maxZ - minZ))

            # Add a grid to the view
            # gls_item = gl.GLSurfacePlotItem(x=None,
            #                                 y=None,
            #                                 z=z,
            #                                 shader='shaded',
            #                                 color=(0.5, 0.5, 1, 1))
            gls_item = gl.GLSurfacePlotItem(x=None,
                                            y=None,
                                            z=z,
                                            colors=rgba_img)
            gls_item.scale(x=self.mapScale['x'],
                           y=self.mapScale['y'],
                           z=self.mapScale['z'])
            gls_item.translate(dx=self.mapTranslate['dx'],
                               dy=self.mapTranslate['dy'],
                               dz=self.mapTranslate['dz'])
            self.graphicsView.addItem(gls_item)
            self.depthQueue.append(z)

            # Save data
            '''
            np.set_printoptions(threshold=np.nan)
            with open('save_data.txt', 'w') as f:
                f.write(str(z))
            f.close()
            '''

        except Exception as e:
            print("[error code] update_db\n", e)
            # If IndexError:
            self.axisX += self.initScale['x']
            self.axisY += self.initScale['y']
            print(self.axisX, self.axisY)
            self.update_db()

    def set_timer(self):
        self.timer = QtCore.QTimer()
        self.timer.setSingleShot(False)
        self.timer.timeout.connect(self.real_time_graph)

    def start_timer(self, sec=5000):
        self.timer.start(sec)

    def end_timer(self):
        self.timer.stop()

    def real_time_graph(self):
        try:
            print("[Message] &Start timer thread, Update graph")
            self.start_timer()
            self.update_db()

        except Exception as e:
            print("[error code] update_db\n", e)
            pass

    def open_filePath(self):
        try:
            filePath = QtWidgets.QFileDialog.getOpenFileName(None, 'Load Your Data')
            checkFilePath = filePath[0].split('/')[-2]  # Check the directory(sample_data)
            fileName = filePath[0].split('/')[-1]
            self.label_filePath.setText(fileName)
            fileFormat = fileName.split('.')[-1]
            if fileFormat == 'csv':
                if checkFilePath == 'sample_data':
                    self.sample_data(filePath=filePath[0])
                elif checkFilePath == 'sample_data2':
                    self.sample_data2(filePath=filePath[0])
            elif fileFormat == '':
                pass
            else:
                errorMsg = QtWidgets.QMessageBox.about(None, "Error", "Please select a csv file.")
                self.label_filePath.setText("")

        except Exception as e:
            print("[error code] open_filePath\n", e)
            pass

    def sample_data(self, filePath):
        filePath = filePath
        try:
            f = open('{0}'.format(filePath), 'r')
            csvReader = csv.reader(f)
            data = []
            for row in csvReader:
                data.append(row)
            f.close()
            del data[0]
            firstLatitudeValue = float('{0:.6f}'.format(float(data[0][0])))
            firstLongitudeValue = float('{0:.6f}'.format(float(data[0][1])))
            firstDepthValue = float('{0:.6f}'.format(float(data[0][2])))

            # Data queue
            queueSize = 2
            latitudeQueue = [] * queueSize
            longitudeQueue = [] * queueSize
            depthQueue = [] * queueSize
            # First point(depth)
            dx, dy = int(self.axisX / 2), int(self.axisY / 2)   # Center point
            dxQueue = [dx]
            dyQueue = [dy]
            for i in range(len(data)):
                '''
                latitude  : data[i][0]
                longitude : data[i][1]
                depth     : data[i][2]
                '''
                latitude = float('{0:.6f}'.format(float(data[i][0])))
                longitude = float('{0:.6f}'.format(float(data[i][1])))
                depth = float('{0:.6f}'.format(float(data[i][2])))

                latitudeQueue.append(latitude)
                longitudeQueue.append(longitude)
                depthQueue.append(depth)

                if len(latitudeQueue[-queueSize:]) > 1:
                    distance = locationAPI.distance(latitude1=latitudeQueue[-2:][0],
                                                    longitude1=longitudeQueue[-2:][0],
                                                    latitude2=latitudeQueue[-2:][1],
                                                    longitude2=longitudeQueue[-2:][1])
                    bearing = locationAPI.bearing(latitude1=latitudeQueue[-2:][0],
                                                  longitude1=longitudeQueue[-2:][0],
                                                  latitude2=latitudeQueue[-2:][1],
                                                  longitude2=longitudeQueue[-2:][1])
                    direction = locationAPI.direction2(bearing=bearing)
                    dx =  dx + direction['dx']
                    dy = dy + direction['dy']
                    dxQueue.append(dx)
                    dyQueue.append(dy)

            # 3D mapping with depth value
            if len(dxQueue) == len(dyQueue) == len(depthQueue):
                # depthQueue2 = [self.axisZ - depthQueue[0]]
                depthQueue2 = [depthQueue[0]]
                for i in range(len(depthQueue)):
                    '''
                    The latitude and longitude below are normalized data
                    that determines the direction on the 3D graph.
                    '''
                    latitude = dxQueue[i]
                    longitude = dyQueue[i]
                    depth = depthQueue[i]
                    # depth = self.axisZ - depth
                    self.dataArr[latitude, longitude] = depth

                    # Apply smoothing graph
                    '''
                    if locationAPI.direction1: smoothRange = 0
                    elif locationAPI.direction2: smoothRange = 1
                    elif locationAPI.direction3: smoothRange = 1
                    elif locationAPI.direction5: smoothRange = 2
                    '''
                    smoothRange = 1
                    if smoothRange > 0:
                        depthQueue2.append(depth)
                        if (dxQueue[i] == latitude) and (dyQueue[i] == longitude):
                            if len(depthQueue2) > 1:
                                # Mapping 될 지점의 Depth 값은 주변의 Depth 값들의 평균 값을 계산하여 적용
                                # depth = float((depthQueue2[-2:][0] + depthQueue2[-2:][1]) / 2)
                                # Mapping 될 지점의 Depth 값은 주변의 Depth 값들 사이의 float 형 난수를 적용
                                depth = random.uniform(float(depthQueue2[-2:][0]), float(depthQueue2[-2:][1]))

                                # 현재 좌표에 대한 주변 8곳을 현재 좌표의 Depth 값으로 Mapping
                                smoothingPoint = SmoothingGraph().smoothing_point(smoothRange=smoothRange)
                                for i in smoothingPoint:
                                    x = i[0]
                                    y = i[1]
                                    self.dataArr[latitude + x, longitude + y] = depth

                                # pst = SmoothingGraph().partial_smoothing_point(smoothRange=smoothRange)
                                # for pst_num in range(len(pst)):
                                #     for i in pst[pst_num]:
                                #         x = i[0]
                                #         y = i[1]
                                #         self.dataArr[latitude + x, longitude + y] = depth - (pst_num + .5)
                    else:
                        pass

            # Surface plot data
            z = self.dataArr
            colorMap = self.comboBox_colorMap.currentText()
            cmap = plt.get_cmap(colorMap)
            minZ = np.min(z)
            maxZ = np.max(z)
            rgba_img = cmap((z - minZ) / (maxZ - minZ))

            # Add a grid to the view
            gls_item = gl.GLSurfacePlotItem(x=None,
                                            y=None,
                                            z=z,
                                            shader='shaded',
                                            color=(0.5, 0.5, 1, 1))
            # gls_item = gl.GLSurfacePlotItem(x=None,
            #                                 y=None,
            #                                 z=z,
            #                                 shader='viewNormalColor')
            # gls_item = gl.GLSurfacePlotItem(x=None,
            #                                 y=None,
            #                                 z=z,
            #                                 shader='normalColor')
            # gls_item = gl.GLSurfacePlotItem(x=None,
            #                                 y=None,
            #                                 z=z,
            #                                 colors=rgba_img)
            gls_item.scale(x=self.mapScale['x'],
                           y=self.mapScale['y'],
                           z=self.mapScale['z'])
            gls_item.translate(dx=self.mapTranslate['dx'],
                               dy=self.mapTranslate['dy'],
                               dz=self.mapTranslate['dz'])
            self.graphicsView.addItem(gls_item)
            self.depthQueue.append(z)

            # Save data
            '''
            np.set_printoptions(threshold=np.nan)
            with open('save_data.txt', 'w') as f:
                f.write(str(z))
            f.close()
            '''

        except Exception as e:
            print("[error code] sample_data\n", e)
            # If IndexError:
            self.axisX += self.initScale['x']
            self.axisY += self.initScale['y']
            self.sample_data(filePath=filePath)

    def sample_data2(self, filePath):
        try:
            with open(filePath, 'r') as f:
                csvReader = csv.reader(f)
                data = []
                for row in csvReader:
                    data.append(row)

            del data[0]

            for i in range(len(data)):
                latitude = int(data[i][0])
                longitude = int(data[i][1])
                depth = float(data[i][2])
                self.dataArr[latitude, longitude] = depth

            # Surface plot data
            z = self.dataArr
            colorMap = self.comboBox_colorMap.currentText()
            cmap = plt.get_cmap(colorMap)
            minZ = np.min(z)
            maxZ = np.max(z)
            rgba_img = cmap((z - minZ) / (maxZ - minZ))

            # Add a grid to the view
            # heightColor, shaded, viewNormalColor, edgeHilight, normalColor, balloon
            gls_item = gl.GLSurfacePlotItem(x=None,
                                            y=None,
                                            z=z,
                                            shader='shaded',
                                            color=(0.5, 0.5, 1, 1))
            # gls_item = gl.GLSurfacePlotItem(x=None,
            #                                 y=None,
            #                                 z=z,
            #                                 shader='viewNormalColor')
            # gls_item = gl.GLSurfacePlotItem(x=None,
            #                                 y=None,
            #                                 z=z,
            #                                 colors=rgba_img)
            gls_item.scale(x=self.mapScale['x']*2,
                           y=self.mapScale['y']*2,
                           z=self.mapScale['z'])
            gls_item.translate(dx=self.mapTranslate['dx']*2,
                               dy=self.mapTranslate['dy']*2,
                               dz=self.mapTranslate['dz'])
            self.graphicsView.addItem(gls_item)
            self.depthQueue.append(z)

        except Exception as e:
            print("[error code] sample_data2\n", e)
            pass



if __name__ == "__main__":

    mysql_connector = DBConnector()
    locationAPI = LocationAPI()

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()

    ui = MainForm()
    ui.setupUi(MainWindow)
    ui.connection_events()
    ui.init_3D_surface()
    ui.colorMapUi()
    ui.view_colorBar()

    MainWindow.show()
    sys.exit(app.exec_())

