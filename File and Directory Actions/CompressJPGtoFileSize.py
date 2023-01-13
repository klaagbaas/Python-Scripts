import io
import math
import sys
import os
from PIL import Image

def JPEG_save_with_target_size(im, filename, target):
   '''Save the image as JPEG with the given name at best quality that makes less than 'target' bytes'''

   # Min and Max quality
   q_min, q_max = 20, 100

   # Highest acceptable quality found
   q_acc = -1
   while q_min <= q_max:
      m = math.floor((q_min + q_max) / 2)

      # Encode into memory and get size
      buffer = io.BytesIO()
      im.save(buffer, format='JPEG', quality=m)
      s = buffer.getbuffer().nbytes

      if s <= target:
         q_acc = m
         q_min = m + 1
      elif s > target:
         q_max = m - 1

   # Write to disk at the defined quality
   if q_acc > -1:
      im.save(filename, format='JPEG', quality=q_acc)
   else:
      print('ERROR: No acceptble quality factor found', file=sys.stderr)

# main

## scan the subdirs for files of our specification, jpg
city = 'LIVERPOOL'
source = f'/Volumes/GoogleDrive-116537148341854220400/Shared drives/Descon Master Drive/Vendor Deliveries/Descon 2022 Shutterstock/{city}/Images'
filesize = 20000000
filepath = []
for root, dirs, files in os.walk(source):
    for name in files:
        filepath.append(os.path.join(root, name))

#check file list for images above filesize and resize
for name in filepath:
    if '.jpg' in name:
        if os.path.getsize(name) > filesize:
            print(f'Compressing {name}, [{filepath.index(name)}/{len(filepath)}]')
            image = Image.open(name)
            JPEG_save_with_target_size(image, name, filesize)

print(f'\n*** {city} done!\n')
