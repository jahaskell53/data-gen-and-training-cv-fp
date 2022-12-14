# Data Generation

This repo contains `data_generation.py`, a python script used for generating synthetic data of random letters 
on white backgrounds and labels in the COCO JSON format. The script creates a data_generated folder,
which has all the output images, as well as a data_generated_mask folder, which contains a binary mask
for each character outline inside a subdirectory for each image. 

This repo also contains `coco.py`, a collection of helper functions from [here](https://github.com/waspinator/pycococreator/blob/master/pycococreatortools/pycococreatortools.py) for dealing with COCO JSON data. 
We call the `binary_mask_to_polygon` function from `data_generation.py` in order to convert our binary mask
into a polygon. 

Lastly, this repo contains `visualize.py`, a script from [here](https://github.com/trsvchn/coco-viewer/blob/main/cocoviewer.py) that visualizes your COCO JSON labels on your images by generating an index.html page that contains this visualization. We use this to ensure our data is in the proper format. 