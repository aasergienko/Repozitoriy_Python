import re

def openfile():
    with open ("vojna.txt", "r", encoding="utf-8") as f:
        text = f.read()
        return text

def findtext(openfile):
    text=openfile()
    lines=text.split(". ")
    for line in lines:
        line_found = re.search("\d\d\d\d год", line)
        if line_found:
            print(line)

findtext(openfile)
