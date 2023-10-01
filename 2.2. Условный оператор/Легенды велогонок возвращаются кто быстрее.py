pt = int(input())
vn = int(input())
tl = int(input())
a = [pt, vn, tl]
a.sort(reverse=True)
d = dict({pt: "Петя", vn: "Вася", tl: "Толя"})
sorted(d.items())
print(f"""{d[a[0]]:^24}\n{d[a[1]]:^8}\n{d[a[2]]:>22}\n{"II":>5}{"I":>7}{"III":>9}""")
