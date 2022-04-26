import os

source_dir = "/Volumes/GoogleDrive/Shared drives/US Descon 2021 Master/_LANDMARK_MAINS"
prefix = "_xph_customlandmark-"

for source, dirs, files in os.walk(source_dir):
    for filename in files:
        splitname = filename.split("_")
        newname = prefix + splitname[1]
        print(newname)
        os.rename(os.path.join(source, filename), os.path.join(source, newname))

print("done")
