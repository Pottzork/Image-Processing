import sys
import os
from PIL import Image


image_folder = sys.argv[1]
output_folder = sys.argv[2]

# Creates a new folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)


# Loops through images in specified folder "Pokedex" and converts them to png
for filename in os.listdir(image_folder):
    img = Image.open(f"{image_folder}{filename}")
    clean_name = os.path.splitext(filename)[0]
    img.save(f"{output_folder}{clean_name}.png", "png")
    print("All done!")
