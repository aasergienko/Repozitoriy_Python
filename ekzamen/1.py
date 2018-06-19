import re
import os
start_path = "."
for files in os.walk(start_path):
    print(files)
    f = open(files, encoding="utf-8")
    text = f.read()
    spisok = re.findall("gr=\"[A-Z]{1,}", text) 


    f.close()

with open('1.csv', 'x'):
    pass


