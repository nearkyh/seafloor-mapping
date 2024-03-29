# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1140, 852)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_push = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_push.setGeometry(QtCore.QRect(10, 220, 211, 31))
        self.pushButton_push.setStyleSheet("")
        self.pushButton_push.setObjectName("pushButton_push")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(230, 0, 911, 831))
        self.graphicsView.setObjectName("graphicsView")
        self.label_latitude = QtWidgets.QLabel(self.centralwidget)
        self.label_latitude.setGeometry(QtCore.QRect(10, 100, 81, 29))
        self.label_latitude.setObjectName("label_latitude")
        self.label_longitude = QtWidgets.QLabel(self.centralwidget)
        self.label_longitude.setGeometry(QtCore.QRect(10, 140, 81, 29))
        self.label_longitude.setObjectName("label_longitude")
        self.label_depth = QtWidgets.QLabel(self.centralwidget)
        self.label_depth.setGeometry(QtCore.QRect(10, 180, 81, 29))
        self.label_depth.setObjectName("label_depth")
        self.pushButton_reset = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_reset.setGeometry(QtCore.QRect(10, 790, 211, 31))
        self.pushButton_reset.setStyleSheet("")
        self.pushButton_reset.setObjectName("pushButton_reset")
        self.pushButton_updateDB = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_updateDB.setGeometry(QtCore.QRect(10, 440, 211, 31))
        self.pushButton_updateDB.setStyleSheet("")
        self.pushButton_updateDB.setObjectName("pushButton_updateDB")
        self.comboBox_colorMap = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_colorMap.setGeometry(QtCore.QRect(10, 310, 211, 27))
        self.comboBox_colorMap.setStyleSheet("")
        self.comboBox_colorMap.setCurrentText("")
        self.comboBox_colorMap.setObjectName("comboBox_colorMap")
        self.pushButton_connectDB = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_connectDB.setGeometry(QtCore.QRect(10, 400, 211, 31))
        self.pushButton_connectDB.setStyleSheet("")
        self.pushButton_connectDB.setObjectName("pushButton_connectDB")
        self.pushButton_disconnectDB = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_disconnectDB.setGeometry(QtCore.QRect(10, 480, 211, 31))
        self.pushButton_disconnectDB.setStyleSheet("")
        self.pushButton_disconnectDB.setObjectName("pushButton_disconnectDB")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(0, 0, 231, 831))
        self.listWidget.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.listWidget.setObjectName("listWidget")
        self.textEdit_depth = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_depth.setGeometry(QtCore.QRect(110, 180, 111, 31))
        self.textEdit_depth.setObjectName("textEdit_depth")
        self.textEdit_longitude = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_longitude.setGeometry(QtCore.QRect(110, 140, 111, 31))
        self.textEdit_longitude.setObjectName("textEdit_longitude")
        self.label_display = QtWidgets.QLabel(self.centralwidget)
        self.label_display.setGeometry(QtCore.QRect(250, 20, 61, 17))
        self.label_display.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_display.setObjectName("label_display")
        self.label_customData = QtWidgets.QLabel(self.centralwidget)
        self.label_customData.setGeometry(QtCore.QRect(0, 60, 231, 31))
        self.label_customData.setStyleSheet("background-color: rgb(50, 50, 50);\n"
"color: rgb(255, 255, 255);")
        self.label_customData.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_customData.setObjectName("label_customData")
        self.label_mapLayers = QtWidgets.QLabel(self.centralwidget)
        self.label_mapLayers.setGeometry(QtCore.QRect(10, 10, 211, 41))
        self.label_mapLayers.setStyleSheet("font: 75 15pt \"Ubuntu\";")
        self.label_mapLayers.setAlignment(QtCore.Qt.AlignCenter)
        self.label_mapLayers.setObjectName("label_mapLayers")
        self.label_colorMap = QtWidgets.QLabel(self.centralwidget)
        self.label_colorMap.setGeometry(QtCore.QRect(0, 270, 231, 31))
        self.label_colorMap.setStyleSheet("background-color: rgb(50, 50, 50);\n"
"color: rgb(255, 255, 255);")
        self.label_colorMap.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_colorMap.setObjectName("label_colorMap")
        self.label_3DMapping = QtWidgets.QLabel(self.centralwidget)
        self.label_3DMapping.setGeometry(QtCore.QRect(0, 360, 231, 31))
        self.label_3DMapping.setStyleSheet("background-color: rgb(50, 50, 50);\n"
"color: rgb(255, 255, 255);")
        self.label_3DMapping.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_3DMapping.setObjectName("label_3DMapping")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 770, 211, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_demoFile = QtWidgets.QLabel(self.centralwidget)
        self.label_demoFile.setGeometry(QtCore.QRect(0, 530, 231, 31))
        self.label_demoFile.setStyleSheet("background-color: rgb(50, 50, 50);\n"
"color: rgb(255, 255, 255);")
        self.label_demoFile.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_demoFile.setObjectName("label_demoFile")
        self.label_filePath = QtWidgets.QLabel(self.centralwidget)
        self.label_filePath.setGeometry(QtCore.QRect(20, 570, 141, 31))
        self.label_filePath.setStyleSheet("")
        self.label_filePath.setText("")
        self.label_filePath.setObjectName("label_filePath")
        self.pushButton_filePath = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_filePath.setGeometry(QtCore.QRect(180, 570, 41, 31))
        self.pushButton_filePath.setStyleSheet("")
        self.pushButton_filePath.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/open.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_filePath.setIcon(icon)
        self.pushButton_filePath.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_filePath.setObjectName("pushButton_filePath")
        self.listWidget_filePath = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_filePath.setGeometry(QtCore.QRect(10, 570, 161, 31))
        self.listWidget_filePath.setObjectName("listWidget_filePath")
        self.textEdit_latitude = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_latitude.setGeometry(QtCore.QRect(110, 100, 111, 31))
        self.textEdit_latitude.setObjectName("textEdit_latitude")
        self.colorBar = QtWidgets.QGraphicsView(self.centralwidget)
        self.colorBar.setGeometry(QtCore.QRect(1020, 560, 101, 251))
        self.colorBar.setStyleSheet("")
        self.colorBar.setObjectName("colorBar")
        self.listWidget.raise_()
        self.label_latitude.raise_()
        self.pushButton_push.raise_()
        self.label_longitude.raise_()
        self.label_depth.raise_()
        self.pushButton_reset.raise_()
        self.pushButton_updateDB.raise_()
        self.comboBox_colorMap.raise_()
        self.pushButton_connectDB.raise_()
        self.pushButton_disconnectDB.raise_()
        self.textEdit_depth.raise_()
        self.textEdit_longitude.raise_()
        self.label_customData.raise_()
        self.label_mapLayers.raise_()
        self.label_colorMap.raise_()
        self.label_3DMapping.raise_()
        self.line.raise_()
        self.graphicsView.raise_()
        self.label_display.raise_()
        self.label_demoFile.raise_()
        self.pushButton_filePath.raise_()
        self.listWidget_filePath.raise_()
        self.label_filePath.raise_()
        self.textEdit_latitude.raise_()
        self.colorBar.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.comboBox_colorMap.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.listWidget, self.textEdit_longitude)
        MainWindow.setTabOrder(self.textEdit_longitude, self.textEdit_depth)
        MainWindow.setTabOrder(self.textEdit_depth, self.pushButton_push)
        MainWindow.setTabOrder(self.pushButton_push, self.comboBox_colorMap)
        MainWindow.setTabOrder(self.comboBox_colorMap, self.pushButton_connectDB)
        MainWindow.setTabOrder(self.pushButton_connectDB, self.pushButton_updateDB)
        MainWindow.setTabOrder(self.pushButton_updateDB, self.pushButton_disconnectDB)
        MainWindow.setTabOrder(self.pushButton_disconnectDB, self.pushButton_reset)
        MainWindow.setTabOrder(self.pushButton_reset, self.graphicsView)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_push.setText(_translate("MainWindow", "Push"))
        self.label_latitude.setText(_translate("MainWindow", " Latitude"))
        self.label_longitude.setText(_translate("MainWindow", " Longitude"))
        self.label_depth.setText(_translate("MainWindow", " Depth"))
        self.pushButton_reset.setText(_translate("MainWindow", "Reset"))
        self.pushButton_updateDB.setText(_translate("MainWindow", "Update"))
        self.pushButton_connectDB.setText(_translate("MainWindow", "Connect"))
        self.pushButton_disconnectDB.setText(_translate("MainWindow", "Disconnect"))
        self.label_display.setText(_translate("MainWindow", " Display"))
        self.label_customData.setText(_translate("MainWindow", "  Custom Data"))
        self.label_mapLayers.setText(_translate("MainWindow", "Map Layers"))
        self.label_colorMap.setText(_translate("MainWindow", "  Color Map"))
        self.label_3DMapping.setText(_translate("MainWindow", "  3D Mapping"))
        self.label_demoFile.setText(_translate("MainWindow", "  Demo File"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

