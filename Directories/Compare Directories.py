import filecmp

def print_left_only(dcmp):
    for name in dcmp.left_only:
        print("Left_only %s found in %s" % (name, dcmp.left))
    for sub_dcmp in dcmp.subdirs.values():
        print_left_only(sub_dcmp)

def print_right_only(dcmp):
    for name in dcmp.right_only:
        print("Right_only %s found in %s" % (name, dcmp.right))
    for sub_dcmp in dcmp.subdirs.values():
        print_right_only(sub_dcmp)

dcmp = filecmp.dircmp(r'c:\Users\Kaspar\Desktop\Portals', r'c:\Users\Kaspar\Desktop\Portals2') 

print_left_only(dcmp)
print_right_only(dcmp)
