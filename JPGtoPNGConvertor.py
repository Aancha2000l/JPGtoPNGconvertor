import sys
import os
from PIL import Image

# grab first nd 2nd argument
image_folder = sys.argv[1]
output_folder = sys.argv[2]

# check if new/ exists, if not create it
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# loop through through pokedex
for filename in os.listdir(image_folder):
    img = Image.open(f'{image_folder}{filename}')
    # by this only the filename will be selected .jpg will be removed so that we r left with just png
    clean_name = os.path.splitext(filename)[0]
# save to new folder
    img.save(f'{output_folder}{clean_name}.png', 'png')
    print("all done!!!!!!!!!!")
