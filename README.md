# Overview

This repo contains code for the "TensorFlow for poets 2" series of Google Codelabs.

### Compile Updated .UI File
pyuic5 Project3UI.ui -o Project3UI.py


### Run Application GUI
python3 runGUI.py

### Retrain Code
python -m scripts.retrain \
  --bottleneck_dir=tf_files/bottlenecks \
  --model_dir=tf_files/models/"${ARCHITECTURE}" \
  --summaries_dir=tf_files/training_summaries/"${ARCHITECTURE}" \
  --output_graph=tf_files/retrained_graph.pb \
  --output_labels=tf_files/retrained_labels.txt \
  --image_dir=tf_files/PHOTO_DIR

### Classify Image
python -m scripts.label_image \
    --image=tf_files/IMG_URL

### Sample (Pretrained) tf_files directory
https://cis.gvsu.edu/~bakercad/ai/tf_files.zip
