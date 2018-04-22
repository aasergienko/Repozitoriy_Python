import os
import re
def count_folders(string):
    file_list = os.listdir(string)
    file_list = set(file_list)
    array = list()
    file_list = list(file_list)
    for c in file_list:
        if os.path.isdir(string + "/" + c):
            a = re.findall("[А-я]", c)
            b = re.findall("[A-z]", c)
            if len(a) > 0 and len(b) > 0:
                array.append(c)
    return len(array)
print(count_folders("C:/test"))