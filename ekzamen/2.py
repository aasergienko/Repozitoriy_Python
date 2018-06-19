import re
import os
def abbrev():

    start_path = "."
    for files in os.walk(start_path):
        print(files)
        f = open(files, encoding="utf-8")
        text = f.read()
        
        spisok = re.search("lex=([А-Я])", text)
        if r:
            spisok.append(spisok.group(1))
        f.close()
    return spisok
spisok = abbrev()
schet = collections.counter(spisok)


def kss():
    table=[]
    with open('2.css', 'x'):
    pass
    with open('2.css', 'w', encoding='utf-8')


