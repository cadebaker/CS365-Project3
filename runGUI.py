import sys
import os
import subprocess
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtGui import QIcon, QPixmap
from Project3UI import Ui_MainWindow
sys.path.insert(0, './scripts')
from label_image_gui import classifyMain


"""
This class handles interaction between the GUI and the backend scripts for
the Tensorflow classification and training.
"""
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    """
    Handles connecting the UI elements to the methods below
    """
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

    """
    Method to select individual file for classification
    """
    def selectFile(self, val2):
        self.resultsDataLabel.setText("")
        global file
        file = QFileDialog.getOpenFileName()[0]
        self.imageLabel.setText(file)
        pixmap = QPixmap(file).scaledToWidth(461);
        self.imageLabel.setPixmap(pixmap)

    """
    Converts decimal to percent
    @param val the value to convert
    @return the decimal number in percent format
    """
    def convertToPercent(self, val):
        return "{:.3%}".format(val)

    """
    Classifies the image using Tensorflow and trained library. Then displays relevant
    detail link
    """
    def runClassify(self):
        if(file != ''):
            returnedClassifyData = classifyMain(file)
            print("------ Classify Results ------")
            template = "{} {:0.5f}"
            for i in range(len(returnedClassifyData)):
                print(template.format(returnedClassifyData[i][0], returnedClassifyData[i][1]))
            viewDetails = ""
            self.resultsDataLabel.setOpenExternalLinks(True)
            if(returnedClassifyData[0][0] == "camaro"):
                viewDetails = "<a href=\"https://www.chevrolet.com/performance/camaro-sports-car/build-and-price/features/trims/table?section=Mechanical&styleOne=401406\"> <font face=verdana font-size=8 color=black>View Details</font> </a>"
                
            elif(returnedClassifyData[0][0] == "corvette"):
                viewDetails = "<a href=\"https://www.chevrolet.com/performance/corvette-stingray-sports-car/build-and-price/features/trims/table?section=Mechanical&styleOne=397566\"> <font face=verdana font-size=8 color=black>View Details</font> </a>"
                
            elif(returnedClassifyData[0][0] == "silverado"):
                viewDetails = "<a href=\"https://www.chevrolet.com/trucks/silverado-1500-pickup-truck/build-and-price/features/trims/table?section=Mechanical&styleOne=399782\"> <font face=verdana font-size=8 color=black>View Details</font> </a>"
                
            elif(returnedClassifyData[0][0] == "malibu"):
                viewDetails = "<a href=\"https://www.chevrolet.com/cars/malibu-mid-size-car/build-and-price/features/trims/table?section=Mechanical&styleOne=402209\"> <font face=verdana font-size=8 color=black>View Details</font> </a>"
                
            elif(returnedClassifyData[0][0] == "tahoe"):
                viewDetails = "<a href=\"https://www.chevrolet.com/suvs/tahoe-full-size-suv/build-and-price/features/trims/table?section=Mechanical&styleOne=400414\"> <font face=verdana font-size=8 color=black>View Details</font> </a>"

            elif(returnedClassifyData[0][0] == "traverse"):
                viewDetails = "<a href=\"https://www.chevrolet.com/suvs/traverse-mid-size-suv/build-and-price/features/trims/table?section=Highlights&styleOne=399663\"> <font face=verdana font-size=8 color=black>View Details</font> </a>"
            
            self.resultsDataLabel.setText("The top result was " + returnedClassifyData[0][0] + " with a probability of " + self.convertToPercent(returnedClassifyData[0][1]) + '. ' + viewDetails)
        else:
            self.resultsDataLabel.setText("Please select an image")

    """
    Select the folder for retraining the model
    """
    def selectFolder(self, val2):
        self.resultsDataLabel.setText("")
        global folder
        folder = str(QFileDialog.getExistingDirectory(self, "Select Directory"))

    """
    Run the training script and notify user whether or not it was successful.
    """
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
