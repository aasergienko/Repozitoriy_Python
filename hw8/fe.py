import random
reply = ["Вы правы", "правильный ответ", "Ответ верен"]
reply_false = ["Вы не правы", "неправильный ответ", "Ответ не верен"]
l = dict({'тает...' : "снег" ,"накрапывал..." : "дождь", "двадцатиградусный..." : "мороз", "тропическая..." : "жара", "снежная..." : "метель"})
for c in l:
    print(c)
    answer = str(input())
    if answer == l.get(c):
        print(random.choic(ereply))
    else:
        print(random.choice(reply_false))
    
