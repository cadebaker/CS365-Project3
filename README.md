# Overview
This repo contains code for the "TensorFlow for poets 2" series of Google Codelabs.<br/>
This application can retrain a model using images (JPG, JPEG, PNG) in the following directory structure:<br/>>
|-- Photos Folder
    |-- Type of Photos Folder
        |-- Actual Image

An example of this is:<br/>>
|-- Cars
    |-- Camaro
        |-- camaro1.JPG

Those images are then used to classify other images. All of this is accomplished using the GUI.

### Required Packages:
NumPy - pip3 install numpy<br/>
TensorFlow - pip3 install --upgrade tensorflow<br/>
Six - pip3 install six<br/>
PyQt5 - pip3 install pyqt5<br/>
Project3UI & label_image_gui (Included)<br/>
Others (likely included): __future__, argparse, collections, datetime, hashlib, os, random, re, sys, tarfile, subprocess, time


### Run Application GUI
python3 runGUI.py

### Sample (Pretrained) tf_files directory
https://cis.gvsu.edu/~bakercad/ai/tf_files.zip
