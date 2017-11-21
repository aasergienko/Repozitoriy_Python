with open("text.txt", encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines:
        a = line.count(" ") + 1

        words = line.split(" ")
        slovo = words[0]
        c = str(a)
        with open("data.csv", "w", encoding="utf-8") as b:
            b.write(slovo + '\t' + c + '\n')

    
