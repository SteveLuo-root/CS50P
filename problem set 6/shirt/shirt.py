import sys
import os
from PIL import Image, ImageOps

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

input_extension = os.path.splitext(sys.argv[1])[1].lower()
output_extension = os.path.splitext(sys.argv[2])[1].lower()
extensions = [".jpg", ".jpeg", ".png"]

if input_extension not in extensions or output_extension not in extensions:
    sys.exit("Invalid input")
if input_extension != output_extension:
    sys.exit("Input and output have different extensions")

try:
    photo = Image.open(sys.argv[1])
    shirt = Image.open("shirt.png")
    photo = ImageOps.fit(photo, size = shirt.size)
    photo.paste(shirt, shirt)
    photo.save(sys.argv[2])
    
except FileNotFoundError:
    sys.exit("Input does not exist")
