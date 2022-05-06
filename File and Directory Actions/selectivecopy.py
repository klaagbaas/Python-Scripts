'''
scan source folder and subfolder contents
if filepath contains 'landmark', name doesn't end with *-001.jpg
and name isn't in dest folder,copy file to destination folder
'''

import shutil
import os

source = '/Volumes/GoogleDrive/Shared drives/US Descon 2021 Master/Shutterstock/1. PHOTO'
dest = '/Volumes/GoogleDrive/Shared drives/US Descon 2021 Master/_LANDMARK_ADDITIONAL'
dirname = 'Landmarks'
filepath_source = []
filepath_dest = []
for root, dirs, files in os.walk(source): #scan files in source directory
    for name in files:
        filepath_source.append(os.path.join(root, name))
        
for root, dirs, files in os.walk(dest): #scan files in destination directory
    for name in files:
        filepath_dest.append(os.path.join(root, name))

for name in filepath_source:
    if dirname in name:
        if '-001' not in name:
            if name not in filepath_dest: #skip files already in the destination directory
                shutil.copy(name, dest)
                print(name)
print("done")
