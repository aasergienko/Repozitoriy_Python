f = open("Ozhegov.txt", encoding="utf-8")
lines = f.readlines()
i=0
for line in lines:
    u = line.find("||")
    stroka = line[0:u]
    slova = stroka.split("|")
    if len(slova) >= 3:
        slovo = slova[2]
        i=i+1
        
print(i)
f.close
