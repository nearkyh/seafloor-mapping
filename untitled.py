# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import pyqtgraph as pg
import numpy as np
import color_bar

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1145, 833)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")


        self.graphicsView = pg.GraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(490, 30, 271, 721))
        self.graphicsView.setObjectName("graphicsView")

        # make colormap
        stops = np.r_[-1.0, -0.5, 0.5, 1.0]
        colors = np.array([[0, 0, 1, 0.7], [0, 1, 0, 0.2], [0, 0, 0, 0.8], [1, 0, 0, 1.0]])
        cm = pg.ColorMap(stops, colors)

        # make colorbar, placing by hand
        cb = color_bar.ColorBar(cm, 20, 200, label='Foo (Hz)')  # , [0., 0.5, 1.0])
        self.graphicsView.scene().addItem(cb)
        # cb.translate(570.0, 90.0)

        self.openGLWidget = QtWidgets.QOpenGLWidget(self.centralwidget)
        self.openGLWidget.setGeometry(QtCore.QRect(150, 30, 300, 721))
        self.openGLWidget.setObjectName("openGLWidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1145, 31))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

