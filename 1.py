with open("text.txt") as f:
    text=f.read()
    print(text.count(". "))
    a=int(0)
    b=int(0)
    for letter in text:
        if letter == 'а' or letter == 'о' or letter =='е' or letter == 'у' or letter == 'ю' or letter == 'ы' or letter == 'я' or letter == 'ё'or letter == 'э':
            a=a+1
        else:
            b=b+1

    print(a, b)
print(text.count(""))
