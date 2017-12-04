stroka = input()
spisok = stroka.split(" ")
with open("slova.txt", "w", encoding="utf-8") as f:
    i=1;
    for string in spisok:

        f.write(string)
        
        if i % 2 == 0:
            f.write("\n")
        i=i+1
