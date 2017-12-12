print("Введите слово")
a = input()

f = open("Ozhegov.txt", encoding="utf-8")
lines = f.readlines()
i=0
for line in lines:

    slova = line.split("|")
    slovo = slova[0]
    if slovo == a:
        i=1
        slovo1 = slova[1]
        slovo2 = slova[2]
        if len(slova)>3:
            slovo3 = slova[3]
            print(slovo, "--", slovo1, "--", slovo2, slovo3)
        else:
            print(slovo, "--", slovo1, "--", slovo2)
        

if i == 0:
    print("Такого слова нет!")
f.close
