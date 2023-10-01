flag = True
k = 0
while flag:
    s = input()
    if s == "Приехали!":
        flag = False
    else:
        if "зайка" in s:
            k += 1
print(k)
