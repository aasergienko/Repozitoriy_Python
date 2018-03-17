import re

def open_file():
    with open("knr.txt", encoding="utf-8") as f:
        text = f.read()
        ready_text = text.split()
    return ready_text

def scan_file(ready_text):
    for word in ready_text:
        r = re.search("^[йцкнгшщзхфвпрлджчсмтб]([уёеыаоэяию])(.\\1)+$", word)
        if r:
            print(word)
            
ready_text = open_file()
scan_file(ready_text)

        
