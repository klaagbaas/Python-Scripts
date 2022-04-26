import os

source_dir = "./rename test"
prefix = "_xph_customlandmark-"
suffix = "-001"

for source, dirs, files in os.walk(source_dir):
    for filename in files:
        splitname = filename.split("_")
        newname = prefix + splitname[1] + suffix
        print(newname)
        os.rename(os.path.join(source, filename), os.path.join(source, newname))

print("done")
