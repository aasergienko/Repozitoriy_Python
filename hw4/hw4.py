f = open("text.txt", encoding="utf-8")
lines = f.readlines()
b=float(0)
c=float(0)
a=float(0)
for line in lines:
    a = 0
    b = b+1
    a = line.count(" ")+1
    if a > 5:
        c = c + 1
d = (c/b)*100
print(d)
