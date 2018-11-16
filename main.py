# -*- coding: utf-8 -*-

'''
    Form implementation generated from reading ui file 'main.ui'
    python -m PyQt5.uic.pyuic -x main.ui -o ui.py
    Created by: PyQt5 UI code generator 5.11.3
    WARNING! All changes made in this file will be lost!
'''

import sys
import numpy as np
import pandas as pd
import csv
import matplotlib.pyplot as plt
import threading

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from pyqtgraph.Qt import QtCore, QtGui

import pyqtgraph as pg
import pyqtgraph.opengl as gl

from utils.db_connector import DBConnector


class Ui_MainWindow(object):

    def __init__(self):
        self.axisX = 50
        self.axisY = 50
        self.axisZ = 50.0
        self.dataArr = np.zeros([self.axisX, self.axisY])
        self.depthQueue = []
        self.colorMap = 'jet'
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

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(998, 780)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_push = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_push.setGeometry(QtCore.QRect(820, 250, 91, 31))
        self.pushButton_push.setObjectName("pushButton_push")
        # self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView = gl.GLViewWidget(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(20, 60, 711, 691))
        self.graphicsView.setObjectName("graphicsView")
        self.pushButton_loadFile = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_loadFile.setGeometry(QtCore.QRect(640, 20, 91, 31))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/open.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_loadFile.setIcon(icon)
        self.pushButton_loadFile.setObjectName("pushButton_loadFile")
        self.listWidget_customData = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_customData.setGeometry(QtCore.QRect(750, 60, 231, 231))
        self.listWidget_customData.setObjectName("listWidget_customData")
        self.label_inputData = QtWidgets.QLabel(self.centralwidget)
        self.label_inputData.setGeometry(QtCore.QRect(820, 80, 91, 17))
        self.label_inputData.setObjectName("label_inputData")
        self.label_latitude = QtWidgets.QLabel(self.centralwidget)
        self.label_latitude.setGeometry(QtCore.QRect(770, 120, 81, 29))
        self.label_latitude.setObjectName("label_latitude")
        self.textEdit_latitude = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_latitude.setGeometry(QtCore.QRect(860, 120, 97, 31))
        self.textEdit_latitude.setObjectName("textEdit_latitude")
        self.textEdit_longtitude = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_longtitude.setGeometry(QtCore.QRect(860, 160, 97, 31))
        self.textEdit_longtitude.setObjectName("textEdit_longtitude")
        self.textEdit_depth = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_depth.setGeometry(QtCore.QRect(860, 200, 97, 31))
        self.textEdit_depth.setObjectName("textEdit_depth")
        self.label_longtitude = QtWidgets.QLabel(self.centralwidget)
        self.label_longtitude.setGeometry(QtCore.QRect(770, 160, 81, 29))
        self.label_longtitude.setObjectName("label_longtitude")
        self.label_depth = QtWidgets.QLabel(self.centralwidget)
        self.label_depth.setGeometry(QtCore.QRect(770, 200, 81, 29))
        self.label_depth.setObjectName("label_depth")
        self.pushButton_reset = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_reset.setGeometry(QtCore.QRect(750, 720, 231, 31))
        self.pushButton_reset.setObjectName("pushButton_reset")
        self.pushButton_updateDB = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_updateDB.setGeometry(QtCore.QRect(760, 470, 211, 31))
        self.pushButton_updateDB.setObjectName("pushButton_updateDB")
        self.listWidget_filePath = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_filePath.setGeometry(QtCore.QRect(20, 20, 611, 31))
        self.listWidget_filePath.setObjectName("listWidget_filePath")
        self.label_filePath = QtWidgets.QLabel(self.centralwidget)
        self.label_filePath.setGeometry(QtCore.QRect(30, 20, 591, 31))
        self.label_filePath.setText("")
        self.label_filePath.setObjectName("label_filePath")
        self.label_colorMap = QtWidgets.QLabel(self.centralwidget)
        self.label_colorMap.setGeometry(QtCore.QRect(750, 310, 231, 21))
        self.label_colorMap.setAlignment(QtCore.Qt.AlignCenter)
        self.label_colorMap.setObjectName("label_colorMap")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(750, 300, 231, 81))
        self.listWidget.setObjectName("listWidget")
        self.comboBox_colorMap = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_colorMap.setGeometry(QtCore.QRect(760, 340, 211, 27))
        self.comboBox_colorMap.setCurrentText("")
        self.comboBox_colorMap.setObjectName("comboBox_colorMap")
        self.listWidget_2 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_2.setGeometry(QtCore.QRect(750, 390, 231, 161))
        self.listWidget_2.setObjectName("listWidget_2")
        self.label_database = QtWidgets.QLabel(self.centralwidget)
        self.label_database.setGeometry(QtCore.QRect(750, 400, 231, 21))
        self.label_database.setAlignment(QtCore.Qt.AlignCenter)
        self.label_database.setObjectName("label_database")
        self.pushButton_connectDB = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_connectDB.setGeometry(QtCore.QRect(760, 430, 211, 31))
        self.pushButton_connectDB.setObjectName("pushButton_connectDB")
        self.pushButton_disconnectDB = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_disconnectDB.setGeometry(QtCore.QRect(760, 510, 211, 31))
        self.pushButton_disconnectDB.setObjectName("pushButton_disconnectDB")
        self.listWidget_2.raise_()
        self.listWidget.raise_()
        self.listWidget_customData.raise_()
        self.graphicsView.raise_()
        self.pushButton_loadFile.raise_()
        self.label_inputData.raise_()
        self.label_latitude.raise_()
        self.textEdit_latitude.raise_()
        self.textEdit_longtitude.raise_()
        self.textEdit_depth.raise_()
        self.pushButton_push.raise_()
        self.label_longtitude.raise_()
        self.label_depth.raise_()
        self.pushButton_reset.raise_()
        self.pushButton_updateDB.raise_()
        self.listWidget_filePath.raise_()
        self.label_filePath.raise_()
        self.label_colorMap.raise_()
        self.comboBox_colorMap.raise_()
        self.label_database.raise_()
        self.pushButton_connectDB.raise_()
        self.pushButton_disconnectDB.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.comboBox_colorMap.setCurrentIndex(-1)
        self.pushButton_loadFile.clicked.connect(self.open_path)
        self.pushButton_push.clicked.connect(self.update_customData)
        self.pushButton_reset.clicked.connect(self.reset_graph)
        self.pushButton_updateDB.clicked.connect(self.update_db)
        self.comboBox_colorMap.currentIndexChanged['QString'].connect(self.update_colorMap)
        self.comboBox_colorMap.setCurrentIndex(len(self.colorMaps['Perceptually Uniform Sequential']) +
                                               len(self.colorMaps['Sequential']) +
                                               len(self.colorMaps['Sequential (2)']) +
                                               len(self.colorMaps['Diverging']) +
                                               len(self.colorMaps['Qualitative']) +
                                               14 + 5)
        self.pushButton_disconnectDB.clicked.connect(self.disconnect_db)
        self.pushButton_connectDB.clicked.connect(self.connect_db)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Default
        self.init_3D_surface()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_push.setText(_translate("MainWindow", "Push"))
        self.pushButton_loadFile.setText(_translate("MainWindow", " Load File"))
        self.label_inputData.setText(_translate("MainWindow", "Custom Data"))
        self.label_latitude.setText(_translate("MainWindow", "Latitude"))
        self.label_longtitude.setText(_translate("MainWindow", "Longtitude"))
        self.label_depth.setText(_translate("MainWindow", "Depth"))
        self.pushButton_reset.setText(_translate("MainWindow", "Reset"))
        self.pushButton_updateDB.setText(_translate("MainWindow", "Update"))
        self.label_colorMap.setText(_translate("MainWindow", "ColorMap"))
        self.label_database.setText(_translate("MainWindow", "Database"))
        self.pushButton_connectDB.setText(_translate("MainWindow", "Connect"))
        self.pushButton_disconnectDB.setText(_translate("MainWindow", "Disconnect"))

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

    def open_path(self):
        try:
            fileName = QFileDialog.getOpenFileName(None, 'Load Your Data')
            self.label_filePath.setText(fileName[0])
            self.load_3D_surface(data=fileName[0])

        except Exception as e:
            print("[error code] open_path\n", e)
            pass

    def update_customData(self):
        try:
            del self.graphicsView.items[2:]
            self.init_3D_surface()
            self.custom_3D_surface()

        except Exception as e:
            print("[error code] update_customData\n", e)
            pass

    def reset_graph(self):
        try:
            self.reset_3D_surface()

        except Exception as e:
            print("[error code] reset_graph\n", e)
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
                np.seterr(divide='ignore', invalid='ignore')    # ignore(main.py:246: RuntimeWarning: invalid value encountered in true_divide)
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
            gls_item = gl.GLSurfacePlotItem(x=None, y=None, z=z, shader='normalColor', color=(0.5, 0.5, 1, 1))
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

                # Surface plot data
                self.dataArr[latitude, longitude] = depth
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

            # print("timer test")
            # threading.Timer(5, self.connect_db).start()

        except Exception as e:
            print("[error code] connect_db\n", e)
            pass

    def disconnect_db(self):
        try:
            pass

        except Exception as e:
            print("[error code] disconnect_db\n", e)
            pass

        finally:
            print("connect_db.exit()")
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

                # Surface plot data
                self.dataArr[latitude, longitude] = depth
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

    def start(self):
        print("start")
        if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
            QtGui.QApplication.instance().exec_()

    def animation(self):
        timer = QtCore.QTimer()
        timer.timeout.connect(self.connect_db)
        timer.start(20)
        self.start()



if __name__ == "__main__":

    mysql_connector = DBConnector()
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
