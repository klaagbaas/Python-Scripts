import os

source_dir = "/Volumes/GoogleDrive/Shared drives/US Descon 2021 Master/_DISTRICT_MAINS"
prefix = "_xph_customdistrict-"
suffix = "-001.jpg"

for source, dirs, files in os.walk(source_dir):
    for filename in files:
        splitname = filename.split("_")
        tempname = splitname[1].split("-")
        newname = prefix + tempname[0] + suffix
        print(newname)
        os.rename(os.path.join(source, filename), os.path.join(source, newname))

print("done")
