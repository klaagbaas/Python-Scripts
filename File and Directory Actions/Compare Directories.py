import filecmp

def print_left_only(dcmp): #prints files that are only in the left (1st) folder
    for name in dcmp.left_only:
        print("Left_only %s found in %s" % (name, dcmp.left))
    for sub_dcmp in dcmp.subdirs.values():
        print_left_only(sub_dcmp)

def print_right_only(dcmp): #prints files that are only in the right (2nd) folder
    for name in dcmp.right_only:
        print("Right_only %s found in %s" % (name, dcmp.right))
    for sub_dcmp in dcmp.subdirs.values():
        print_right_only(sub_dcmp)

dcmp = filecmp.dircmp(r'c:\leftdir', r'c:\rightdir') 

print_left_only(dcmp)
# print_right_only(dcmp)
