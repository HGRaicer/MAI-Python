pt = int(input())
vn = int(input())
tl = int(input())
a = [pt, vn, tl]
a.sort(reverse=True)
d = dict({pt: "Петя", vn: "Вася", tl: "Толя"})
sorted(d.items())
for i in range(len(a)):
    print(f"{i+1}. {d[a[i]]}")
