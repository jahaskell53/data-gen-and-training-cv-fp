# Model Training

This repo contains `CS1430_Final_Project_Model.ipynb`, a jupyter notebook that we modified from [here](https://www.immersivelimit.com/tutorials/using-mask-r-cnn-on-custom-coco-like-dataset) for training our model. We added comments to this notebook, created our own algorithms for determining which characters make up a word, called google translate's API and created our own algorithms for overlaying translated in the same location as the original text. We also trained our model using this script on Google Colab. 

At the start of the notebook we clone our fork (which can be found [here](https://github.com/Ayma-n/Mask_RCNN)) of the Mask_RCNN library which we use in the notebook, as there were initially many compatibility issues that prevented use of the original library, so we had to make many adjustments to the source code. 

## Link to Weights

[Here](https://drive.google.com/file/d/1hQRv1TzoWhG6BkHsGcikilGNnCin4doY/view?usp=sharing) is a Google Drive link to the weights we generated using the Jupyter Notebook and we used for our final model. 

# Data Generation

This repo contains `data_generation.py`, a python script used for generating synthetic data of random letters 
on white backgrounds and labels in the COCO JSON format. The script creates a data_generated folder,
which has all the output images, as well as a data_generated_mask folder, which contains a binary mask
for each character outline inside a subdirectory for each image. 

This repo also contains `coco.py`, a collection of helper functions from [here](https://github.com/waspinator/pycococreator/blob/master/pycococreatortools/pycococreatortools.py) for dealing with COCO JSON data. 
We call the `binary_mask_to_polygon` function from `data_generation.py` in order to convert our binary mask
into a polygon. 

Lastly, this repo contains `visualize.py`, a script from [here](https://github.com/trsvchn/coco-viewer/blob/main/cocoviewer.py) that visualizes your COCO JSON labels on your images by generating an index.html page that contains this visualization. We use this to ensure our data is in the proper format. 

## Link to Data

[Here](https://drive.google.com/file/d/1L9Wj-wxc3tILjDKdJJgY8IPTNbZCPd-P/view?usp=sharing) is a Google Drive link to training and testing data that we generated using this script and used for our final model. 