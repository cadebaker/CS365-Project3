# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Project3UI.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(801, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.mainHeader = QtWidgets.QLabel(self.centralwidget)
        self.mainHeader.setGeometry(QtCore.QRect(0, 0, 801, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(40)
        self.mainHeader.setFont(font)
        self.mainHeader.setAlignment(QtCore.Qt.AlignCenter)
        self.mainHeader.setObjectName("mainHeader")
        self.trainFolderButton = QtWidgets.QTabWidget(self.centralwidget)
        self.trainFolderButton.setGeometry(QtCore.QRect(-10, 90, 800, 481))
        self.trainFolderButton.setObjectName("trainFolderButton")
        self.tab = QtWidgets.QWidget()
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.tab.setFont(font)
        self.tab.setObjectName("tab")
        self.classifyLabel = QtWidgets.QLabel(self.tab)
        self.classifyLabel.setGeometry(QtCore.QRect(50, 40, 151, 16))
        self.classifyLabel.setObjectName("classifyLabel")
        self.chooseFile = QtWidgets.QPushButton(self.tab)
        self.chooseFile.setGeometry(QtCore.QRect(50, 70, 141, 23))
        self.chooseFile.setObjectName("chooseFile")
        self.imageLabel = QtWidgets.QLabel(self.tab)
        self.imageLabel.setGeometry(QtCore.QRect(270, 22, 461, 261))
        self.imageLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.imageLabel.setScaledContents(False)
        self.imageLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.imageLabel.setObjectName("imageLabel")
        self.classifyButton = QtWidgets.QPushButton(self.tab)
        self.classifyButton.setGeometry(QtCore.QRect(50, 150, 141, 23))
        self.classifyButton.setObjectName("classifyButton")
        self.resultsDataLabel = QtWidgets.QLabel(self.tab)
        self.resultsDataLabel.setGeometry(QtCore.QRect(40, 315, 701, 81))
        self.resultsDataLabel.setText("")
        self.resultsDataLabel.setObjectName("resultsDataLabel")
        self.trainFolderButton.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setStrikeOut(False)
        self.tab_2.setFont(font)
        self.tab_2.setObjectName("tab_2")
        self.trainingFolderButton = QtWidgets.QPushButton(self.tab_2)
        self.trainingFolderButton.setGeometry(QtCore.QRect(250, 60, 321, 23))
        self.trainingFolderButton.setObjectName("trainingFolderButton")
        self.runTrainingButton = QtWidgets.QPushButton(self.tab_2)
        self.runTrainingButton.setGeometry(QtCore.QRect(250, 120, 321, 23))
        self.runTrainingButton.setObjectName("runTrainingButton")
        self.trainingResults = QtWidgets.QLabel(self.tab_2)
        self.trainingResults.setGeometry(QtCore.QRect(20, 200, 771, 231))
        self.trainingResults.setText("")
        self.trainingResults.setObjectName("trainingResults")
        self.trainFolderButton.addTab(self.tab_2, "")
        self.namesHeader = QtWidgets.QLabel(self.centralwidget)
        self.namesHeader.setGeometry(QtCore.QRect(200, 60, 401, 21))
        self.namesHeader.setAlignment(QtCore.Qt.AlignCenter)
        self.namesHeader.setObjectName("namesHeader")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 801, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        self.trainFolderButton.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Image Classify GUI"))
        self.mainHeader.setText(_translate("MainWindow", "Image Classify GUI"))
        self.classifyLabel.setText(_translate("MainWindow", "Choose File to Classify:"))
        self.chooseFile.setText(_translate("MainWindow", "Select File"))
        self.imageLabel.setText(_translate("MainWindow", "Select Image"))
        self.classifyButton.setText(_translate("MainWindow", "Run Classification"))
        self.trainFolderButton.setTabText(self.trainFolderButton.indexOf(self.tab), _translate("MainWindow", "Classify"))
        self.trainingFolderButton.setText(_translate("MainWindow", "Training Folder"))
        self.runTrainingButton.setText(_translate("MainWindow", "Run Training"))
        self.trainFolderButton.setTabText(self.trainFolderButton.indexOf(self.tab_2), _translate("MainWindow", "Retrain"))
        self.namesHeader.setText(_translate("MainWindow", "By: Cade Baker, Megan Thomas, Brendan Nahed"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))

