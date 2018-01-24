import random
def nouns1():
    f=open("nouns1.txt", encoding="utf-8")
    text=f.read()
    text1 = text.split()
    return random.choice(text1)
    f.close()
def verbs1():
    f=open("verbs1.txt", encoding="utf-8")
    text=f.read()
    text1 = text.split()
    return random.choice(text1)
def nouns2():
    f=open("nouns2.txt", encoding="utf-8")
    text=f.read()
    text1 = text.split()
    return random.choice(text1)
def verbs2():
    f=open("verbs2.txt", encoding="utf-8")
    text=f.read()
    text1 = text.split()
    return random.choice(text1)
def stroka5():
    return nouns1() + ' ' + verbs1() + ','
def stroka7():
    return nouns2() + ' ' + verbs2() + '.'


print(stroka5())
print(stroka7())
print(stroka5())
print(stroka7())
print(stroka7())
