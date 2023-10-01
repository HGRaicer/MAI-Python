n = int(input())
m = int(input())

pt = 7
vc = 6
pt -= 3
vc += 3
pt += 2
vc += 5
vc -= 2
pt += n
vc += m
if pt > vc:
    print("Петя")
else:
    print("Вася")
