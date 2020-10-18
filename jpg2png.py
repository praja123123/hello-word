import sys
from os import walk, mkdir, path
from PIL import Image
import re

jpg_folder = sys.argv[1]
png_folder = sys.argv[2]
# jpg_folder = './pokemon'
# png_folder = './pokemon_png'

file_ext = 'png'

if path.isdir(png_folder):
    pass
else:
    mkdir(png_folder)

pattern = re.compile(r'.+\.jpg')

files = []

for (dirpath, dirnames, filenames) in walk(jpg_folder):
    files.extend(filenames)
    break

for file in files:
    if pattern.fullmatch(file):
        img = Image.open(f'{jpg_folder}/{file}')
        file_name = file.split('.')[0]
        print(file_name)
        img.save(f'{png_folder}/{file_name}.{file_ext}', 'png')
