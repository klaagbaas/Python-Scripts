import os

source_dir = "/Volumes/GoogleDrive/Shared drives/US Descon 2021 Master/_LANDMARK_ADDITIONAL"
prefix = "_xph_customlandmark-"

for source, dirs, files in os.walk(source_dir):
    for filename in files:
        if filename.startswith(prefix): #if the file in the directory already has the right naming convention, skip it
            continue
        else:
            filename2 = filename.replace("-","_") # easy way to make these files splittable on one delimiter
            splitname = filename2.split("_")
            newname = prefix + splitname[1] + "-" + splitname[2] # add the file number back in (-00x)
            print(newname)
            os.rename(os.path.join(source, filename), os.path.join(source, newname))

print("done")
