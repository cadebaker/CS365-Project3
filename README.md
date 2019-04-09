# Overview
This repo contains code for the "TensorFlow for poets 2" series of Google Codelabs.
This application can retrain a model using images (JPG, JPEG, PNG) in the following directory structure:
> Photos Folder
  > Type of Photos Folder
    > Actual Image
  > Type of Photos Folder
    > Actual Image

An example of this is:
> Cars
  > Camaro
    > camero1.JPG
  > Malibu
    >malibu1.JPEG

Those images are then used to classify other images. All of this is accomplished using the GUI.

### Required Packages:
NumPy - pip3 install numpy
TensorFlow - pip3 install --upgrade tensorflow
Six - pip3 install six
PyQt5 - pip3 install pyqt5
Project3UI & label_image_gui (Included)
Others (likely included): __future__, argparse, collections, datetime, hashlib, os, random, re, sys, tarfile, subprocess, time


### Run Application GUI
python3 runGUI.py

### Sample (Pretrained) tf_files directory
https://cis.gvsu.edu/~bakercad/ai/tf_files.zip
