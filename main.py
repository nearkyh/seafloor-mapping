# -*- coding: utf-8 -*-

'''
    Form implementation generated from reading ui file 'main.ui'
    python -m PyQt5.uic.pyuic -x main.ui -o ui.py
    Created by: PyQt5 UI code generator 5.11.3
    WARNING! All changes made in this file will be lost!

    Add the following method to ui.py:
    import pyqtgraph.opengl as gl
    self.graphicsView = gl.GLViewWidget(self.centralwidget)

'''

import sys
import numpy as np
np.seterr(divide='ignore', invalid='ignore')
import pandas as pd
import csv

import pyqtgraph as pg
import pyqtgraph.opengl as gl
import matplotlib.pyplot as plt

from PyQt5 import QtCore, QtGui, QtWidgets
from pyqtgraph.Qt import QtCore, QtGui

from ui import Ui_MainWindow
from utils.db_connector import DBConnector


class MainForm(Ui_MainWindow):

    def __init__(self):
        super(MainForm, self).__init__()

        self.axisX = 50
        self.axisY = 50
        self.axisZ = 50.0
        self.dataArr = np.zeros([self.axisX, self.axisY])
        self.depthQueue = []
        self.colorMap = 'ocean'
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

    def connection_events(self):
        self.pushButton_loadFile.clicked.connect(self.open_filePath)
        self.pushButton_push.clicked.connect(self.update_customData)
        self.pushButton_reset.clicked.connect(self.reset_data)
        self.comboBox_colorMap.currentIndexChanged['QString'].connect(self.update_colorMap)
        self.pushButton_connectDB.clicked.connect(self.connect_db)
        self.pushButton_updateDB.clicked.connect(self.update_db)
        self.pushButton_disconnectDB.clicked.connect(self.disconnect_db)

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

    def open_filePath(self):
        try:
            fileName = QtWidgets.QFileDialog.getOpenFileName(None, 'Load Your Data')
            self.label_filePath.setText(fileName[0])
            self.load_3D_surface(data=fileName[0])

        except Exception as e:
            print("[error code] open_filePath\n", e)
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
                gls_item = gl.GLSurfacePlotItem(x=None, y=None, z=z, colors=rgba_img)
                gls_item.scale(x=.5, y=.5, z=.5)
                gls_item.translate(-10, -10, 0)
                self.graphicsView.addItem(gls_item)

        except Exception as e:
            print("[error code] update_colorMap\n", e)
            pass

    def init_3D_surface(self):
        try:
            # Set graphics view
            self.graphicsView.show()
            self.graphicsView.setBackgroundColor('k')
            self.graphicsView.setCameraPosition(distance=50, elevation=None, azimuth=None)

            # Add a grid to the view
            g = gl.GLGridItem()
            g.scale(x=2, y=2, z=1)
            g.setDepthValue(10) # draw grid after surfaces since they may be translucent
            self.graphicsView.addItem(g)

            # Simple surface plot example
            z = np.array([[0]])
            # z = np.array([[-50, 0, -50],
            #               [0, 50, 0],
            #               [0, 0, 0]])
            # z = np.array([
            #     [1000, 1200, 1400, 1100],
            #     [1000, 1200, 1400, 1100],
            #     [1400, 1400, 1400, 1100],
            #     [1000, 1400, 1400, 1100]])
            colorMap = self.comboBox_colorMap.currentText()
            cmap = plt.get_cmap(self.colorMap)
            minZ = np.min(z)
            maxZ = np.max(z)
            rgba_img = cmap((z - minZ) / (maxZ - minZ))

            # plt.imshow(z, cmap=cmap)
            # plt.colorbar()
            # plt.clim(minZ, maxZ)
            # plt.show()

            # gls_item = gl.GLSurfacePlotItem(x=None, y=None, z=z, shader='normalColor', color=(0.5, 0.5, 1, 1))
            gls_item = gl.GLSurfacePlotItem(x=None, y=None, z=z, colors=rgba_img)
            gls_item.scale(x=.5, y=.5, z=.5)  # x, y, z 비율값
            gls_item.translate(-10, -10, 0)  # 시작점 (x, y, z)
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
            longtitude = self.textEdit_longtitude.toPlainText()
            longtitude = int(longtitude)
            depth = self.textEdit_depth.toPlainText()
            depth = float(depth)
            depth = self.axisZ - depth

            # Surface plot data
            self.dataArr[latitude, longtitude] = depth
            z = self.dataArr
            colorMap = self.comboBox_colorMap.currentText()
            cmap = plt.get_cmap(colorMap)
            minZ = np.min(z)
            maxZ = np.max(z)
            rgba_img = cmap((z - minZ) / (maxZ - minZ))

            # Add a grid to the view
            # gls_item = gl.GLSurfacePlotItem(x=None, y=None, z=z, smooth=True, shader='normalColor', glOptions='opaque')
            gls_item = gl.GLSurfacePlotItem(x=None, y=None, z=z, colors=rgba_img)
            gls_item.scale(x=.5, y=.5, z=.5)
            gls_item.translate(-10, -10, 0)
            self.graphicsView.addItem(gls_item)
            self.depthQueue.append(z)

            # Reset textEdit
            # if str(latitude):
            #     self.textEdit_latitude.setText("")
            # if str(longtitude):
            #     self.textEdit_longtitude.setText("")
            # if str(depth):
            #     self.textEdit_depth.setText("")

        except Exception as e:
            print("[error code] custom_3D_surface\n", e)
            pass

    def load_3D_surface(self, data):
        try:
            if data:
                # Load surface plot data
                rowArr = []
                f = open('{0}'.format(data), 'r')
                csvReader = csv.reader(f)
                for row in csvReader:
                    row = list(map(float, row))
                    rowArr.append(row)
                f.close()

                # Surface plot data
                # x = np.array([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29])
                # y = np.array([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29])
                z = np.array(rowArr)
                colorMap = self.comboBox_colorMap.currentText()
                cmap = plt.get_cmap(colorMap)
                minZ = np.min(z)
                maxZ = np.max(z)
                rgba_img = cmap((z - minZ) / (maxZ - minZ))

                ## Add a grid to the view
                # gls_item = gl.GLSurfacePlotItem(x=None, y=None, z=z, smooth=True, shader='normalColor', glOptions='opaque')
                # gls_item = gl.GLSurfacePlotItem(x=x, y=y, z=z, colors=rgba_img)
                gls_item = gl.GLSurfacePlotItem(x=None, y=None, z=z, colors=rgba_img)
                gls_item.scale(x=.5, y=.5, z=.5)
                gls_item.translate(-10, -10, 0)
                self.graphicsView.addItem(gls_item)
                self.depthQueue.append(z)

        except Exception as e:
            print('[error code] load_3D_surface\n', e)
            pass

    def reset_3D_surface(self):
        try:
            del self.graphicsView.items[2:]                     # Remove all graphics items
            del self.depthQueue[:]                              # Remove all depth
            self.dataArr = np.zeros([self.axisX, self.axisY])   # Remove all data array (depth)
            self.init_3D_surface()                              # Initialize graph
            self.label_filePath.setText("")
            self.textEdit_latitude.setText("")
            self.textEdit_longtitude.setText("")
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
            self.reset_3D_surface()
            data = mysql_connector.select_data()
            for i in range(len(data)):
                '''
                latitude  : data[i][1]
                longitude : data[i][2]
                depth     : data[i][3]
                '''
                latitude = data[i][1]
                longitude = data[i][2]
                depth = float(data[i][3])
                self.dataArr[latitude, longitude] = depth

            # Surface plot data
            z = self.dataArr
            colorMap = self.comboBox_colorMap.currentText()
            cmap = plt.get_cmap(colorMap)
            minZ = np.min(z)
            maxZ = np.max(z)
            rgba_img = cmap((z - minZ) / (maxZ - minZ))

            ## Add a grid to the view
            gls_item = gl.GLSurfacePlotItem(x=None, y=None, z=z, colors=rgba_img)
            gls_item.scale(x=.5, y=.5, z=.5)
            gls_item.translate(-10, -10, 0)
            self.graphicsView.addItem(gls_item)
            self.depthQueue.append(z)

        except Exception as e:
            print("[error code] update_db\n", e)
            pass

    def set_timer(self):
        self.timer = QtCore.QTimer()
        self.timer.setSingleShot(False)
        self.timer.timeout.connect(self.real_time_graph)

    def start_timer(self, sec=10000):
        self.timer.start(sec)

    def end_timer(self):
        self.timer.stop()

    def real_time_graph(self):
        try:
            print("[Message] &Start timer thread, Update graph")
            self.start_timer()
            self.reset_3D_surface()
            data = mysql_connector.select_data()
            for i in range(len(data)):
                '''
                latitude  : data[i][1]
                longitude : data[i][2]
                depth     : data[i][3]
                '''
                latitude = data[i][1]
                longitude = data[i][2]
                depth = float(data[i][3])
                self.dataArr[latitude, longitude] = depth

            # Surface plot data
            z = self.dataArr
            colorMap = self.comboBox_colorMap.currentText()
            cmap = plt.get_cmap(colorMap)
            minZ = np.min(z)
            maxZ = np.max(z)
            rgba_img = cmap((z - minZ) / (maxZ - minZ))

            ## Add a grid to the view
            gls_item = gl.GLSurfacePlotItem(x=None, y=None, z=z, colors=rgba_img)
            gls_item.scale(x=.5, y=.5, z=.5)
            gls_item.translate(-10, -10, 0)
            self.graphicsView.addItem(gls_item)
            self.depthQueue.append(z)

        except Exception as e:
            print("[error code] update_db\n", e)
            pass



if __name__ == "__main__":

    mysql_connector = DBConnector()

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()

    ui = MainForm()
    ui.setupUi(MainWindow)
    ui.connection_events()
    ui.init_3D_surface()
    ui.colorMapUi()
    ui.set_timer()

    MainWindow.show()
    sys.exit(app.exec_())
