import sys
import os
import subprocess
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtGui import QIcon, QPixmap
from Project3UI import Ui_MainWindow
sys.path.insert(0, './scripts')
from label_image_gui import classifyMain

#qtCreatorFile = "Project3UI.ui" # Enter file here.

#Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.chooseFile.clicked.connect(self.selectFile)
        self.imageLabel.mousePressEvent = self.selectFile
        self.classifyButton.clicked.connect(self.runClassify)
        self.trainingFolderButton.clicked.connect(self.selectFolder)
        self.runTrainingButton.clicked.connect(self.runTrain)
        self.actionExit.triggered.connect(QtCore.QCoreApplication.instance().quit)

    def selectFile(self, val2):
        self.resultsDataLabel.setText("")
        global file
        file = QFileDialog.getOpenFileName()[0]
        self.imageLabel.setText(file)
        pixmap = QPixmap(file).scaledToWidth(461);
        self.imageLabel.setPixmap(pixmap)

    def convertToPercent(self, val):
        return "{:.3%}".format(val)

    def runClassify(self):
        if(file != ''):
            returnedClassifyData = classifyMain(file)
            print("------ Results ------")
            template = "{} {:0.5f}"
            for i in range(len(returnedClassifyData)):
                print(template.format(returnedClassifyData[i][0], returnedClassifyData[i][1]))
            self.resultsDataLabel.setText("The top result was " + returnedClassifyData[0][0] + " with a probability of " + self.convertToPercent(returnedClassifyData[0][1]))
        else:
            self.resultsDataLabel.setText("Please select an image")

    def selectFolder(self, val2):
        self.resultsDataLabel.setText("")
        global folder
        folder = str(QFileDialog.getExistingDirectory(self, "Select Directory"))

    def runTrain(self):
        if(folder != ''):
            print('------ Training Results ------')
            trainResult = os.system('python3 -m scripts.retrain --bottleneck_dir=tf_files/bottlenecks --model_dir=tf_files/models/"${ARCHITECTURE}" --summaries_dir=tf_files/training_summaries/"${ARCHITECTURE}" --output_graph=tf_files/retrained_graph.pb --output_labels=tf_files/retrained_labels.txt --image_dir='+folder)
            if(trainResult == 0):
                self.trainingResults.setText("Training Succeeded")
            else:
                self.trainingResults.setText("An error occurred. Please see console for full output.")

        else:
            self.trainingResults.setText("You must first choose a folder before training.")




if __name__ == "__main__":
    file = ''
    folder = ''
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())