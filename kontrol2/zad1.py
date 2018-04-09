import re
def openfile():
    with open("corpora.xml", encoding="utf-8") as f:
        text = f.read()
        text_ready = f.readlines()
        
    return text_ready

text = openfile()

def find_word(text):
    i = 0
    b = 0
    for line in text:
        i = i + 1
        print (line)
        first_match = re.search("teiHeader", line)
        if first_match:
            b = i
        
    return b



openfile()
find_word(text)
b = find_word(text)
print(b)


        
def write_into(b):
    with open("function.txt", "w", encoding="utf-8") as f:
        f.write(b)
write_into(b)
