a = 0
b = 1001
while True:
    k = (a + b) // 2
    print(k)
    strr = input()
    if strr == "Угадал!":
        break
    elif strr == "Меньше":
        b = k
    else:
        a = k
print("Число отгадано")