import io
import math
import sys
import os
from PIL import Image

def JPEGSaveWithTargetSize(im, filename, target):
   '''Save the image as JPEG with the given name at best quality that makes less than 'target' bytes'''

   # Min and Max quality
   Qmin, Qmax = 20, 100

   # Highest acceptable quality found
   Qacc = -1
   while Qmin <= Qmax:
      m = math.floor((Qmin + Qmax) / 2)

      # Encode into memory and get size
      buffer = io.BytesIO()
      im.save(buffer, format='JPEG', quality=m)
      s = buffer.getbuffer().nbytes

      if s <= target:
         Qacc = m
         Qmin = m + 1
      elif s > target:
         Qmax = m - 1

   # Write to disk at the defined quality
   if Qacc > -1:
      im.save(filename, format='JPEG', quality=Qacc)
   else:
      print('ERROR: No acceptble quality factor found', file=sys.stderr)

# main

## scan the subdirs for files of our specification, jpg
city = 'DENVER'
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
            image = Image.open(name)
            JPEGSaveWithTargetSize(image, name, filesize)
            print('Compressed', name)

print('/n*** Done!/n')
