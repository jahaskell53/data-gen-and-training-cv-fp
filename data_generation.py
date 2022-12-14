import zipfile
import datetime
import string
import math
import os
import shutil
import csv 
import json
import tqdm
import matplotlib.pyplot as plt
import cv2
import keras_ocr
import random as rand
import glob 

from PIL import Image
from PIL import ImageFont, ImageDraw
import numpy as np
from coco import *
data_dir = '.'
alphabet = "abcdefghijklmnopqrstuvwxyz"
print(alphabet)
recognizer_alphabet = ''.join(sorted(set(alphabet.lower())))
# fonts = keras_ocr.data_generation.get_fonts(
#     alphabet=alphabet,
#     cache_dir=data_dir
# )

# backgrounds = keras_ocr.data_generation.get_backgrounds(cache_dir=data_dir)

text_generator = keras_ocr.data_generation.get_text_generator(alphabet=alphabet)
print('The first generated text is:', next(text_generator))
font_list = glob.glob('**/**/*.ttf', recursive=True)

save_directory = "data_generated"
test_folder = "test"
training_folder = "train"
if os.path.exists(save_directory):
    shutil.rmtree(save_directory) # NOTICE: if your directory is empty and you want to delete it, use os.remove(save_directory)
os.mkdir(save_directory)  
# the directory below is for masks
mask_directory = "data_generated_mask"
if os.path.exists(mask_directory):
    shutil.rmtree(mask_directory) # NOTICE: if your directory is empty and you want to delete it, use os.remove(save_directory)
os.mkdir(mask_directory)  

output = {} # rows for json file
output["annotations"] = []
output["images"] = []
output["info"] = { "description": "test_dataset"} # still have to do trainning and testing didfference
output["categories"] = []
for i, char in enumerate(alphabet):
    output["categories"].append({"id": i+1, "name": char})
counter = 1
total_count = 0
maxm = 200
for i in range (maxm): 
    if(counter > maxm):
        break
    image = np.zeros([512,512,3],dtype=np.uint8)
    image.fill(255)
    
    print(image.shape)

    image_height, image_width, _ = image.shape
    # plt.imshow(image)

    # offset = font_size
    # top_right_bound = (x_location + offset, y_location)
    # bottom_left_bound = (x_location, y_location+offset)
    # bottom_right_bound = (x_location + offset, y_location+offset)
    # # draw = ImageDraw.Draw(image)
    img = Image.fromarray(image)
    img = img.crop((0, 0, 256, 256))
    image_height, image_width, _ = 256, 256, 1
    I1 = ImageDraw.Draw(img)

    # create a folder inside mask_directory
    # filename = image_path.split("/")[-1][:-4] # this includes the .jpg ending
    os.mkdir(mask_directory + "/" + str(counter))
    current_image = {}

    current_image["id"] = counter
    current_image["width"] = image_width
    current_image["height"] = image_height
    current_image["file_name"] = str(counter) + ".png"
    output["images"].append(current_image)
    random_int = rand.randint(5,10)
    seen_chars= {}
    for i in range(0, random_int):
        current_annotation = {}
        random_int = rand.randint(0,len(alphabet) - 1)
        random_character = alphabet[random_int]
        if random_character in seen_chars:
            # skip if random character is already used
            # this is needed because we want to name the file with the character
            continue
        seen_chars[random_character] = 1 # add random_character to dict

        red_value = 0
        green_value = 0
        blue_value = 0

        i = rand.randrange(len(font_list))

        # random_font = font_list[i]
        # print(random_font)

        random_font = "helvetica.ttf"

        # font_size = rand.randint(20,40)
        font_size = 25
        y_location = min(image_height - 50, rand.randrange(image_height))
        x_location = min(image_width - 50, rand.randrange(image_width))
        print(y_location, x_location)

        top_left_bound = (x_location, y_location)
        rand_font = ImageFont.truetype(random_font, font_size)
        try:
            I1.text((x_location, y_location), random_character, fill=(red_value, green_value, blue_value), font = rand_font)
        except:
            continue
        # the below code excerpt is taken from here: https://github.com/python-pillow/Pillow/issues/3921 
        right, bottom = rand_font.getsize(random_character)
        width, height = rand_font.getmask(random_character).size
        right += x_location # bottom right x
        bottom += y_location # bottom right y
        top = bottom - height # top left y
        left = right - width # top left x
        current_annotation["id"] = total_count
        current_annotation["iscrowd"] = 0
        current_annotation["image_id"] = counter
        current_annotation["category_id"] = random_int + 1
        # creating a new mask image
        
        mask = Image.new(mode="L", size=(image_width,image_height))
        mask_draw = ImageDraw.Draw(mask)
        mask_draw.text((x_location, y_location), random_character, fill=(255), font = rand_font)
        new_mask = np.array(mask)
        polygon = binary_mask_to_polygon(new_mask)
        current_annotation["segmentation"] = polygon
        current_annotation["bbox"] = [left, top, width, height]
        current_annotation["area"] = width * height
        mask.save(f"{mask_directory}/" + str(counter) + "/" + random_character + ".png")
        output["annotations"].append(current_annotation)
        current_annotation = {}
        total_count+=1
    image = img.save(f"{save_directory}/"  + str(counter) + ".png")
    counter+=1

# writing to CSV
json_filename = "text_box_data.json"
json_relative_file_path = "data_generated/" + json_filename
json_absolute_file_path = os.path.join(save_directory, json_filename)
if os.path.exists(json_relative_file_path):
  os.remove(json_absolute_file_path)

with open(json_absolute_file_path, 'w+') as csvfile:
    csvfile.write(json.dumps(output))