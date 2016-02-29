# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1032, 582)
        MainWindow.setMinimumSize(QtCore.QSize(1032, 582))
        MainWindow.setMaximumSize(QtCore.QSize(1032, 582))
        MainWindow.setStyleSheet("MainWidndow{background: rgb(255, 255, 255)}")
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.tab1 = QtWidgets.QTabWidget(self.centralWidget)
        self.tab1.setGeometry(QtCore.QRect(0, 0, 1031, 521))
        self.tab1.setMinimumSize(QtCore.QSize(1031, 521))
        self.tab1.setMaximumSize(QtCore.QSize(1031, 521))
        self.tab1.setObjectName("tab1")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.line1 = QtWidgets.QLineEdit(self.tab)
        self.line1.setGeometry(QtCore.QRect(510, 20, 381, 41))
        self.line1.setObjectName("line1")
        self.bar1 = QtWidgets.QProgressBar(self.tab)
        self.bar1.setGeometry(QtCore.QRect(240, 20, 261, 41))
        self.bar1.setProperty("value", 24)
        self.bar1.setObjectName("bar1")
        self.tv = QtWebKitWidgets.QWebView(self.tab)
        self.tv.setGeometry(QtCore.QRect(9, 79, 421, 301))
        self.tv.setMinimumSize(QtCore.QSize(421, 301))
        self.tv.setMaximumSize(QtCore.QSize(421, 301))
        self.tv.setUrl(QtCore.QUrl("about:blank"))
        self.tv.setObjectName("tv")
        self.list1 = QtWidgets.QListWidget(self.tab)
        self.list1.setGeometry(QtCore.QRect(435, 81, 591, 401))
        self.list1.setObjectName("list1")
        self.exit = QtWidgets.QPushButton(self.tab)
        self.exit.setGeometry(QtCore.QRect(20, 400, 401, 71))
        self.exit.setObjectName("exit")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(10, 20, 211, 41))
        self.label.setStyleSheet("color: rgb(15, 79, 255);")
        self.label.setObjectName("label")
        self.search = QtWidgets.QPushButton(self.tab)
        self.search.setGeometry(QtCore.QRect(900, 20, 121, 41))
        self.search.setObjectName("search")
        self.tab1.addTab(self.tab, "")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1032, 25))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        self.tab1.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.exit.setText(_translate("MainWindow", "exit"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt;\">BiliBili</span></p></body></html>"))
        self.search.setText(_translate("MainWindow", "search"))
        self.tab1.setTabText(self.tab1.indexOf(self.tab), _translate("MainWindow", "BiliBili Tv"))

from PyQt5 import QtWebKitWidgets
