import re
file = open("text.txt", "r", encoding="utf-8")
count = -1
for line in file:
    count = count - 1
    result = re.match(r"    ISO 639-3", line)
    if result != None:
        count = 2
    if count == 0:
        break
file.close()
file = open("result.txt", "w")
file.write(line)
file.close()