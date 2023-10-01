flag = True
x = 0
y = 0
while flag:
    nap = input()
    if nap == "СТОП":
        flag = False
    else:
        shag = int(input())
        if nap == "СЕВЕР":
            y += shag
        elif nap == "ЮГ":
            y -= shag
        elif nap == "ВОСТОК":
            x += shag
        elif nap == "ЗАПАД":
            x -= shag
print(y, x, sep="\n")
