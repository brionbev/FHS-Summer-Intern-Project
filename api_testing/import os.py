import os 

parent = os.getcwd()
curr_dir = os.path.dirname(os.getcwd())
while (curr_dir != parent):
    # iterates through the parent directory of the current directory
    # until we arrive at the root directory
    parent = os.path.dirname(parent)
    curr_dir = os.path.dirname(curr_dir)
for root, dirs, files in os.walk(parent):
    # iterates through the sub directory of root directory
    # until we arrive at the \data directory
    if 'data' == root.split('\\')[-1]:
        parent = root
        break
print(parent)



