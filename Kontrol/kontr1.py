f = open("Ozhegov.txt", encoding="utf-8")
lines = f.readlines()
for line in lines:
    slova = line.split("|")
    slovo = slova[0]
    if len(slovo) > 20 or len(slovo) == 20:
        print(line)
    
f.close
