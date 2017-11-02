alphabet = 'абвгдеёжзийклмнопрстуфхцчшщьыъэюя'
spisok2=list(alphabet)
slovo=str(input(''))
spisok1=list(slovo)
letter=int()
letter2=int()
if slovo:
    while letter < len(spisok1):
        while letter2 < len(spisok2):
            if spisok1[letter]==spisok2[letter2]:
                spisok3[letter]=spisok2[letter2+1]
    print(spisok3)
    

