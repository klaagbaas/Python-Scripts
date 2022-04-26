'''
scan source folder and subfolder contents
if filepath contains 'landmark', copy *-001.jpg to destination folder
'''

import shutil
import os

source = '/Volumes/GoogleDrive/Shared drives/US Descon 2021 Master/Snapwire/'
dest = '/Volumes/GoogleDrive/Shared drives/US Descon 2021 Master/_LANDMARK_MAINS'
dirname = 'Landmarks'
filepath = []
for root, dirs, files in os.walk(source):
    for name in files:
        filepath.append(os.path.join(root, name))

for name in filepath:
    if dirname in name:
        if '-001' in name:
            shutil.copy(name, dest)
