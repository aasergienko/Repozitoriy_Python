import os
import re
start_path = '.'
number = 0
root_name = ''
string = ''
for root, dirs, files in os.walk(start_path):
    if len(files) > number:
        number = len(files)
        root_name = root
print(root_name[root_name.rfind('\\')+1:])