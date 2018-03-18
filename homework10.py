import re
def openfile():
    with open("text.txt", "r", encoding="UTF-8")as c: 
        whole = c.read()
        ready_text = whole.split()
    return ready_text

ready_text = openfile()
def scan(ready_text):
    for word in ready_text:
        verbs = re.search(r"\b(сид(?:и|ит|ев|ет|ят|иш|ящ|ел|я)[а-я]*)", word)
        if verbs:
            print(word)
openfile()
scan(ready_text)
