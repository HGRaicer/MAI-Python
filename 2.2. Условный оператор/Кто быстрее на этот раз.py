pt = int(input())
vn = int(input())
tl = int(input())
d = dict({pt: "Петя", vn: "Вася", tl: "Толя"})

ma = max(pt, vn, tl)
print(d[ma])

